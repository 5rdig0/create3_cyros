from launch import LaunchDescription
import launch_ros.actions
from launch.actions import DeclareLaunchArgument, OpaqueFunction
from launch.substitutions import LaunchConfiguration

configurable_parameters = [{'name': 'camera_name',                  'default': 'rs', 'description': 'camera unique name'},
                           {'name': 'camera_namespace',             'default': 'Einstein_rs', 'description': 'namespace for camera'},
                           {'name': 'serial_no',                    'default': "''", 'description': 'choose device by serial number'},
                           {'name': 'usb_port_id',                  'default': "''", 'description': 'choose device by usb port id'},
                           {'name': 'device_type',                  'default': "''", 'description': 'choose device by type'},
                           {'name': 'config_file',                  'default': "''", 'description': 'yaml config file'},
                           {'name': 'json_file_path',               'default': "''", 'description': 'allows advanced configuration'},
                           {'name': 'initial_reset',                'default': 'false', 'description': "''"},
                           {'name': 'accelerate_gpu_with_glsl',     'default': "true", 'description': 'enable GPU acceleration with GLSL'},
                           {'name': 'rosbag_filename',              'default': "''", 'description': 'A realsense bagfile to run from as a device'},
                           {'name': 'log_level',                    'default': 'info', 'description': 'debug log level [DEBUG|INFO|WARN|ERROR|FATAL]'},
                           {'name': 'output',                       'default': 'screen', 'description': 'pipe node output [screen|log]'},
                           {'name': 'enable_color',                 'default': 'true', 'description': 'enable color stream'},
                           {'name': 'rgb_camera.color_profile',     'default': '0,0,0', 'description': 'color stream profile'},
                           {'name': 'rgb_camera.color_format',      'default': 'RGB8', 'description': 'color stream format'},
                           {'name': 'rgb_camera.enable_auto_exposure', 'default': 'true', 'description': 'enable/disable auto exposure for color image'},
                           {'name': 'enable_depth',                 'default': 'true', 'description': 'enable depth stream'},
                           {'name': 'enable_infra',                 'default': 'false', 'description': 'enable infra0 stream'},
                           {'name': 'enable_infra1',                'default': 'false', 'description': 'enable infra1 stream'},
                           {'name': 'enable_infra2',                'default': 'false', 'description': 'enable infra2 stream'},
                           {'name': 'depth_module.depth_profile',   'default': '0,0,0', 'description': 'depth stream profile'},
                           {'name': 'depth_module.depth_format',    'default': 'Z16', 'description': 'depth stream format'},
                           {'name': 'depth_module.infra_profile',   'default': '0,0,0', 'description': 'infra streams (0/1/2) profile'},
                           {'name': 'depth_module.infra_format',    'default': 'RGB8', 'description': 'infra0 stream format'},
                           {'name': 'depth_module.infra1_format',   'default': 'Y8', 'description': 'infra1 stream format'},
                           {'name': 'depth_module.infra2_format',   'default': 'Y8', 'description': 'infra2 stream format'},
                           {'name': 'depth_module.exposure',        'default': '8500', 'description': 'Depth module manual exposure value'},
                           {'name': 'depth_module.gain',            'default': '16', 'description': 'Depth module manual gain value'},
                           {'name': 'depth_module.hdr_enabled',     'default': 'false', 'description': 'Depth module hdr enablement flag. Used for hdr_merge filter'},
                           {'name': 'depth_module.enable_auto_exposure', 'default': 'true', 'description': 'enable/disable auto exposure for depth image'},
                           {'name': 'depth_module.exposure.1',      'default': '7500', 'description': 'Depth module first exposure value. Used for hdr_merge filter'},
                           {'name': 'depth_module.gain.1',          'default': '16', 'description': 'Depth module first gain value. Used for hdr_merge filter'},
                           {'name': 'depth_module.exposure.2',      'default': '1', 'description': 'Depth module second exposure value. Used for hdr_merge filter'},
                           {'name': 'depth_module.gain.2',          'default': '16', 'description': 'Depth module second gain value. Used for hdr_merge filter'},
                           {'name': 'enable_sync',                  'default': 'true', 'description': "'enable sync mode'"},
                           {'name': 'enable_rgbd',                  'default': 'true', 'description': "'enable rgbd topic'"},
                           {'name': 'enable_gyro',                  'default': 'false', 'description': "'enable gyro stream'"},
                           {'name': 'enable_accel',                 'default': 'false', 'description': "'enable accel stream'"},
                           {'name': 'gyro_fps',                     'default': '0', 'description': "''"},
                           {'name': 'accel_fps',                    'default': '0', 'description': "''"},
                           {'name': 'unite_imu_method',             'default': "0", 'description': '[0-None, 1-copy, 2-linear_interpolation]'},
                           {'name': 'clip_distance',                'default': '-2.', 'description': "''"},
                           {'name': 'angular_velocity_cov',         'default': '0.01', 'description': "''"},
                           {'name': 'linear_accel_cov',             'default': '0.01', 'description': "''"},
                           {'name': 'diagnostics_period',           'default': '0.0', 'description': 'Rate of publishing diagnostics. 0=Disabled'},
                           {'name': 'publish_tf',                   'default': 'false', 'description': '[bool] enable/disable publishing static & dynamic TF'},
                           {'name': 'tf_publish_rate',              'default': '0.0', 'description': '[double] rate in Hz for publishing dynamic TF'},
                           {'name': 'pointcloud.enable',            'default': 'false', 'description': ''},
                           {'name': 'pointcloud.stream_filter',     'default': '2', 'description': 'texture stream for pointcloud'},
                           {'name': 'pointcloud.stream_index_filter','default': '0', 'description': 'texture stream index for pointcloud'},
                           {'name': 'pointcloud.ordered_pc',        'default': 'false', 'description': ''},
                           {'name': 'pointcloud.allow_no_texture_points', 'default': 'false', 'description': "''"},
                           {'name': 'align_depth.enable',           'default': 'true', 'description': 'enable align depth filter'},
                           {'name': 'colorizer.enable',             'default': 'false', 'description': 'enable colorizer filter'},
                           {'name': 'decimation_filter.enable',     'default': 'false', 'description': 'enable_decimation_filter'},
                           {'name': 'spatial_filter.enable',        'default': 'false', 'description': 'enable_spatial_filter'},
                           {'name': 'temporal_filter.enable',       'default': 'false', 'description': 'enable_temporal_filter'},
                           {'name': 'disparity_filter.enable',      'default': 'false', 'description': 'enable_disparity_filter'},
                           {'name': 'hole_filling_filter.enable',   'default': 'false', 'description': 'enable_hole_filling_filter'},
                           {'name': 'hdr_merge.enable',             'default': 'false', 'description': 'hdr_merge filter enablement flag'},
                           {'name': 'wait_for_device_timeout',      'default': '40.', 'description': 'Timeout for waiting for device to connect (Seconds)'},
                           {'name': 'reconnect_timeout',            'default': '40.', 'description': 'Timeout(seconds) between consequtive reconnection attempts'},
                          ]
parameters_rgb =          [{'name': 'camera_name',                  'default': 'rs', 'description': 'camera unique name'},
                           {'name': 'camera_namespace',             'default': 'Einstein_rs', 'description': 'namespace for camera'},
                           {'name': 'initial_reset',                'default': 'false', 'description': "''"},
                           {'name': 'accelerate_gpu_with_glsl',     'default': "false", 'description': 'enable GPU acceleration with GLSL'},
                           {'name': 'log_level',                    'default': 'info', 'description': 'debug log level [DEBUG|INFO|WARN|ERROR|FATAL]'},
                           {'name': 'enable_color',                 'default': 'true', 'description': 'enable color stream'},
                           {'name': 'rgb_camera.color_profile',     'default': '0,0,0', 'description': 'color stream profile'},
                           {'name': 'rgb_camera.color_format',      'default': 'RGB8', 'description': 'color stream format'},
                           {'name': 'enable_depth',                 'default': 'false', 'description': 'enable depth stream'},
                           {'name': 'wait_for_device_timeout',      'default': '40.', 'description': 'Timeout for waiting for device to connect (Seconds)'},
                           {'name': 'reconnect_timeout',            'default': '40.', 'description': 'Timeout(seconds) between consequtive reconnection attempts'},
                          ]
parameters_depth =        [{'name': 'camera_name',                  'default': 'rs', 'description': 'camera unique name'},
                           {'name': 'camera_namespace',             'default': 'Einstein_rs', 'description': 'namespace for camera'},
                           {'name': 'initial_reset',                'default': 'false', 'description': "''"},
                           {'name': 'accelerate_gpu_with_glsl',     'default': "false", 'description': 'enable GPU acceleration with GLSL'},
                           {'name': 'log_level',                    'default': 'info', 'description': 'debug log level [DEBUG|INFO|WARN|ERROR|FATAL]'},
                           {'name': 'enable_color',                 'default': 'true', 'description': 'enable color stream'},
                           {'name': 'rgb_camera.color_profile',     'default': '0,0,0', 'description': 'color stream profile'},
                           {'name': 'rgb_camera.color_format',      'default': 'RGB8', 'description': 'color stream format'},
                           {'name': 'enable_depth',                 'default': 'false', 'description': 'enable depth stream'},
                           {'name': 'wait_for_device_timeout',      'default': '40.', 'description': 'Timeout for waiting for device to connect (Seconds)'},
                           {'name': 'reconnect_timeout',            'default': '40.', 'description': 'Timeout(seconds) between consequtive reconnection attempts'},
                          ]
def declare_configurable_parameters(parameters):
    return [DeclareLaunchArgument(param['name'], default_value=param['default'], description=param['description']) for param in parameters]

def set_configurable_parameters(parameters):
    return dict([(param['name'], LaunchConfiguration(param['name'])) for param in parameters])

def launch_setup(context, params, param_name_suffix=''):
    _output = LaunchConfiguration('output' + param_name_suffix)
    return [
        launch_ros.actions.Node(
            package='realsense2_camera',
            namespace=LaunchConfiguration('camera_namespace' + param_name_suffix),
            name=LaunchConfiguration('camera_name' + param_name_suffix),
            executable='realsense2_camera_node',
            parameters=[params],
            output=_output,
            arguments=['--ros-args', '--log-level', LaunchConfiguration('log_level' + param_name_suffix)],
            emulate_tty=True,
        ),
        # launch_ros.actions.Node(
        #     package='rs_cam',
        #     namespace='Einstein_rs',
        #     name='detect',
        #     executable='detect',
        # ),
    ]

def generate_launch_description():
    return LaunchDescription(declare_configurable_parameters(configurable_parameters) + [
        OpaqueFunction(function=launch_setup, kwargs = {'params' : set_configurable_parameters(configurable_parameters)})
    ])