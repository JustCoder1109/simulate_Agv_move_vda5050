# 协作规则

## 动作前询问（强制）

在任何**写操作或命令执行**之前，必须先询问用户并获得明确同意，得到同意后才可执行。

需要先询问的动作包括：

- 创建、修改、删除、移动任何文件
- 执行任何 shell / docker / ros2 / colcon 命令
- git 操作（包括 add、commit、checkout、push 等）
- 安装或卸载依赖、修改系统或容器配置

只读操作（读文件、列目录、搜索代码、查看 git 状态与日志）无需询问，直接执行。

询问时需说明：要做什么、为什么做、影响范围；批量操作应整体说明后再询问。

# 项目与环境事实

## 资料分布（四层）

1. **总体资料**：Windows 项目文件夹（项目需求、资料手册、工具），虚拟机内不可直接访问；使用时需用户拷入 `docs/` 或粘贴/截图到对话。
2. **开发仓库**：vm-ubuntu 主机路径 `/home/rk3568/hzt_practise/simulate_Agv_move_vda5050`，受 git 管理（分支 main，远端 `git@github.com:JustCoder1109/simulate_Agv_move_vda5050.git`）。
3. **开发容器**：`ros2_agv_vda5050`（见下节），`ros2_ws` 作为数据卷挂载，容器内路径 `/root/ros2_ws`。
4. **目标板**：调试通过后将 `ros2_ws` 中的节点代码移植到板端（板型号/架构/ROS 版本待补充）。

## 容器固定事实

| 项 | 值 |
|---|---|
| 容器名 | `ros2_agv_vda5050` |
| 镜像 | `docker.m.daocloud.io/osrf/ros:humble-desktop-full` |
| ROS 发行版 | Humble（`ROS_DISTRO=humble`，容器内为用户 root） |
| 网络 | host 模式，`DISPLAY=:0`，挂载 `/tmp/.X11-unix`（GUI 可用） |
| 卷映射 | 宿主机 `ros2_ws` ↔ 容器 `/root/ros2_ws` |
| 工具 | `ros2` CLI、`colcon`（/usr/bin/colcon）均可用 |
| MCP | `.mcp.json` 已配置 atomicviz（http://127.0.0.1:3939/mcp） |

常用命令模板：

```bash
# 构建整个工作空间
docker exec ros2_agv_vda5050 bash -lc 'source /opt/ros/humble/setup.bash && cd /root/ros2_ws && colcon build'
# 只构建指定包
docker exec ros2_agv_vda5050 bash -lc 'source /opt/ros/humble/setup.bash && cd /root/ros2_ws && colcon build --packages-select <pkg>'
# 运行节点
docker exec ros2_agv_vda5050 bash -lc 'source /opt/ros/humble/setup.bash && source /root/ros2_ws/install/setup.bash && ros2 run <pkg> <node>'

echo "source /root/ros2_ws/install/setup.bash" >> ~/.bashrc
```

容器重建方式见仓库 `README`（需先 `xhost +local:docker`）。

## 开发约定

- 源码在宿主机 `ros2_ws/` 下编辑（git 追踪），构建与运行在容器内执行。
- 首次构建前需创建 `.gitignore` 排除 `ros2_ws/build/`、`ros2_ws/install/`、`ros2_ws/log/`。
- GUI 工具（rviz2、gazebo）依赖 X11 转发，需宿主机桌面会话处于活动状态。
- 板端移植前提：节点不依赖桌面组件，依赖写入 `package.xml`，注意 x86 → ARM 与 Humble 版本一致性。