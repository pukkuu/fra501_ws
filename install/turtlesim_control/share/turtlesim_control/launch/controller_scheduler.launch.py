from launch import LaunchDescription, LaunchContext
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument, ExecuteProcess, OpaqueFunction
from launch.substitutions import LaunchConfiguration
from ament_index_python.packages import get_package_share_directory
import os
import yaml

def modify_config_namespace(path:str, new_path:str, namespace:str) -> None:
    with open(path, 'r') as file:
        data = yaml.load(file, Loader=yaml.SafeLoader)
    new_data = {namespace: data}
    with open(new_path, 'w') as file:
        yaml.dump(new_data, file)

def render_node(
        context:LaunchContext,
        launch_description:LaunchDescription,
        pkg:str,
        execute:str,
        name:LaunchConfiguration,
        param:str,
        arg
) -> None:
    node_pkg = get_package_share_directory(pkg)
    if type(arg) == LaunchConfiguration:
        arg_str = context.perform_substitution(arg)
        arg_path = os.path.join(node_pkg, arg_str)
        print(arg_path)
    else:
        arg_path = ''
        
    param_path = ''
    if len(param):
        name_str = context.perform_substitution(name)
        sprit_param = param.split('.')
        config_param_path = os.path.join(node_pkg, param)
        param_path = os.path.join(node_pkg, sprit_param[0] + '_' + name_str + '.yaml')
        modify_config_namespace(config_param_path, param_path, name_str)

    node = Node(
        package=pkg,
        executable=execute,
        namespace=name,
        parameters=[param_path],
        arguments=['-f', arg_path]
    )
    launch_description.add_action(node)

def generate_launch_description():

    launch_description = LaunchDescription()

    x_launch_arg = DeclareLaunchArgument('x', default_value='5.0')
    y_launch_arg = DeclareLaunchArgument('y', default_value='5.0')
    name_launch_arg  = DeclareLaunchArgument('name')
    file_launch_arg = DeclareLaunchArgument('file')
    x = LaunchConfiguration('x')
    y = LaunchConfiguration('y')
    name = LaunchConfiguration('name')
    file = LaunchConfiguration('file')

    cmd = LaunchConfiguration('cmd', default=[
        'ros2 service call /spawn turtlesim/srv/Spawn "{x: ',
        x,
        ', y: ',
        y,
        ', theta: 0.0, name: \'',
        name,
        '\'}"'
    ])
    spawn_turtle = ExecuteProcess(cmd= [[cmd]], shell=True)

    kill_turtle = ExecuteProcess(cmd= ["ros2 service call /kill turtlesim/srv/Kill \"{name: 'turtle1'}\""], shell=True)

    turtlesim = Node( 
        package='turtlesim', 
        executable='turtlesim_node'
    )

    controller_opaque_function = OpaqueFunction(
        function=render_node,
        args=[launch_description,
              'turtlesim_control',
              'controller.py',
              name,
              'config/controller_config.yaml',
              '']
    )

    scheduler_opaque_function = OpaqueFunction(
        function=render_node,
        args=[launch_description,
              'turtlesim_control',
              'scheduler.py',
              name,
              '',
              file]
    )

    launch_description.add_action(turtlesim)
    launch_description.add_action(controller_opaque_function)
    launch_description.add_action(scheduler_opaque_function)
    launch_description.add_action(x_launch_arg)
    launch_description.add_action(y_launch_arg)
    launch_description.add_action(name_launch_arg)
    launch_description.add_action(file_launch_arg)
    launch_description.add_action(kill_turtle)
    launch_description.add_action(spawn_turtle)
    return launch_description