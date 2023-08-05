from typing import Dict, Any, List
from typing import Callable
import awswrangler as aw
import glob, os, subprocess, setuptools, list_imports, boto3, sys, importlib, inspect, logging

logger = logging.getLogger(__name__)

auto_execute: bool = True


def disable_auto_execute():
    global auto_execute
    auto_execute = False


def enable_auto_execute():
    global auto_execute
    auto_execute = True


class GlueJobItem:
    def __init__(
        self,
        function: Callable[..., None],
        name: str,
        region: str,
        role: str,
        job_path: str,
        lib_path: str,
        description: str = "",
        execution_property: Dict[str, Any] = {"MaxConcurrentRuns": 1},
        command: Dict[str, str] = {"Name": "pythonshell", "PythonVersion": "3"},
        default_arguments: Dict[str, Any] = {},
        connections: Dict[str, Any] = {"Connections": []},
        max_retries: int = 2,
        timeout: int = 2880,
        max_capacity: float = 1.0,
        security_configuration: str = "",
        tags: Dict[str, str] = {},
        notification_property: Dict[str, Any] = {"NotifyDelayAfter": 10},
        glue_version: str = "1.0",
        number_of_workers: int = 2,
        worker_type: str = "Standard",
    ):
        self._function = function
        self._name = name
        self._region = region
        self._role = role
        self._description = description
        self._execution_property = execution_property
        self._command = command
        self._default_arguments = default_arguments
        self._connections = connections
        self._max_retries = max_retries
        self._timeout = timeout
        self._max_capacity = max_capacity
        self._security_configuration = security_configuration
        self._tags = tags
        self._notification_property = notification_property
        self._glue_version = glue_version
        self._number_of_workers = number_of_workers
        self._worker_type = worker_type
        self._job_path = job_path
        self._lib_path = lib_path

    def publish_job(self, session: aw.Session):
        local_file_path = inspect.getfile(self._function)
        local_lib_setup_path = ".cache/setup-" + self._name + ".py"
        required_libraries = list(list_imports.get(local_file_path))
        setup_content = """\
import setuptools

setuptools.setup(
    name={0},
    version="1.0",
    packages=setuptools.find_packages(),       
    python_requires="==3.6.8",
    install_requires={1},
    zip_safe=True,
)
""".format(
            self._name, required_libraries
        )

        with open(local_lib_setup_path, "w") as file:
            file.write(setup_content)
            
        dist = setuptools.Distribution(dict(
            script_name=local_lib_setup_path,
            script_args=["bdist_egg"],
            name=self._name,
            install_requires=required_libraries
        ))
        
        dist.parse_command_line()
        dist.run_commands()

        egg_file = glob.glob("dist/{0}*.egg".format(self._name))[0]

        session.s3.write_file(egg_file, self._lib_path)
        session.s3.write_file(local_file_path, self._job_path)
        session.glue.create_job(self)


declared_jobs: List[GlueJobItem] = []


def glue_job(
    name: str,
    region: str,
    role: str,
    job_path: str,
    lib_path: str,
    description: str = "",
    execution_property: Dict[str, Any] = {"MaxConcurrentRuns": 1},
    command: Dict[str, str] = {"Name": "pythonshell", "PythonVersion": "3"},
    default_arguments: Dict[str, Any] = {},
    connections: Dict[str, Any] = {"Connections": []},
    max_retries: int = 2,
    timeout: int = 2880,
    max_capacity: float = 1.0,
    security_configuration: str = "",
    tags: Dict[str, str] = {},
    notification_property: Dict[str, Any] = {"NotifyDelayAfter": 10},
    glue_version: str = "1.0",
    number_of_workers: int = 2,
    worker_type: str = "Standard",
    auto_execute: bool = auto_execute,
):
    """Wraps a method as a glue job. The method will be executed on import as if it was a script using the given DefaultArguments.
    
    Arguments:
        Name {str} -- The name you assign to this job definition. It must be unique in your account.
        Role {str} -- The name or Amazon Resource Name (ARN) of the IAM role associated with this job.

    
    Keyword Arguments:
        Description {str} -- Description of the job being defined.    
        ExecutionProperty {Dict[str,Any]} -- An ExecutionProperty specifying the maximum number of concurrent runs allowed for this job. (default: {{"MaxConcurrentRuns": 1}})
        Command {Dict[str,str]} -- The JobCommand that executes this job. (default: {{"Name": "pythonshell", "PythonVersion": "3"}})
        DefaultArguments {Dict[str,Any]} -- The default arguments for this job.
        You can specify arguments here that your own job-execution script consumes, 
        as well as arguments that AWS Glue itself consumes. (default: {{}})
        Connections {Dict[str,Any]} -- [description] (default: {{"Connections": []}})
        MaxRetries {int} -- [description] (default: {2})
        Timeout {int} -- [description] (default: {2880})
        MaxCapacithy {float} -- [description] (default: {1.0})
        SecurityConfiguration {str} -- [description] (default: {""})
        Tags {Dict[str,str]} -- [description] (default: {{}})
        NotificationProperty {Dict[str,Any]} -- [description] (default: {{"NotifyDelayAfter": 10}})
        GlueVersion {str} -- [description] (default: {"1.0"})
        NumberOfWorkers {int} -- [description] (default: {2})
        WorkerType {str} -- [description] (default: {"Standard"})
    """

    def decorator(function: Callable[..., None]):
        logger.info("Registering glue job with method: {0}".format(function.__name__))
        declared_jobs.append(
            GlueJobItem(
                function=function,
                name=name,
                region=region,
                role=role,
                description=description,
                execution_property=execution_property,
                job_path=job_path,
                lib_path=lib_path,
                command={**command, "ScriptLocation": job_path},
                default_arguments={**default_arguments, "--extra-py-files": lib_path},
                connections=connections,
                max_retries=max_retries,
                timeout=timeout,
                max_capacity=max_capacity,
                security_configuration=security_configuration,
                tags=tags,
                notification_property=notification_property,
                glue_version=glue_version,
                number_of_workers=number_of_workers,
                worker_type=worker_type,
            )
        )

        function_args = list(function.__code__.co_varnames)

        logger.info("Required args: {0}".format(function_args))

        if importlib.util.find_spec("awsglue") != None:
            logger.debug("Module awsglue detected.")
            from awsglue.utils import getResolvedOptions

            args = getResolvedOptions(sys.argv, function_args)
            target_args = {key: args[key] for key in function_args}
            logger.info(
                "Module awsglue was detected, using resolved args: {0}".format(
                    target_args
                )
            )
        else:
            target_args = default_arguments
            logger.info(
                "Module awsglue was not detected, using default args: {0}".format(
                    target_args
                )
            )

        if auto_execute:
            logger.info("Job execution started.")
            function(**target_args)
            logger.info("Job completed successfully.")

    return decorator
