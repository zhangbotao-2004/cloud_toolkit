\# Cloud Toolkit — 云服务管理工具



> 一个命令行工具，整合 Nginx 自动化部署和 EC2 实例管理。



\## 项目简介



`cloud-toolkit` 是一个 Python 编写的命令行工具，将你之前四个项目（手动部署 Nginx、自动化部署 Nginx、EC2 模拟管理、综合管理工具）整合成一个统一入口。通过一条命令即可完成 Nginx 部署、状态查看、EC2 模拟等操作。



\## 技术栈



\- \*\*Python 3\*\*

\- \*\*subprocess\*\* — 调用子模块

\- \*\*argparse / sys.argv\*\* — 命令行参数解析

\- \*\*colorama\*\*（可选）— 彩色输出

\- \*\*Nginx / Ubuntu\*\* — 目标管理环境

\- \*\*Boto3 + Moto\*\* — EC2 模拟



\## 功能列表



| 命令 | 说明 |

|------|------|

| `nginx` | 完整部署 Nginx（安装 + 端口修改 80→8080 + 验证） |

| `nginx-status` | 查看 Nginx 服务状态 |

| `ec2` | 运行 EC2 实例管理模拟（创建 → 停止 → 启动） |

| `menu` | 交互式菜单模式（适合不熟悉命令的用户） |

| `list` | 列出所有可用命令 |

| `help` | 显示完整帮助信息 |



\## 项目结构



```

cloud-toolkit/

├── cloud-toolkit.py      # 主程序

├── nginx_manager.py      # Nginx 管理模块

├── ec2_manager.py        # EC2 管理模块

├── README.md

└── 截图/

&#x20;   ├── screenshot_help.png

&#x20;   ├── screenshot_list.png

&#x20;   ├── screenshot_nginx_status.png

&#x20;   └── screenshot_ec2.png

```



\## 运行方法



\### 1. 安装依赖

```bash

pip3 install colorama   # 可选，用于彩色输出

```



\### 2. 进入项目目录

```bash

cd /mnt/shared/cloud-toolkit   # 或你实际的路径

```



\### 3. 查看帮助

```bash

python3 cloud-toolkit.py help

```



\### 4. 列出所有命令

```bash

python3 cloud-toolkit.py list

```



\### 5. 使用命令

```bash

\# 完整部署 Nginx

python3 cloud-toolkit.py nginx



\# 查看 Nginx 状态

python3 cloud-toolkit.py nginx-status



\# 运行 EC2 模拟

python3 cloud-toolkit.py ec2



\# 交互式菜单

python3 cloud-toolkit.py menu

```



\## 项目截图
## 项目截图

### 帮助信息
![帮助信息](./截图/screenshot_help.png)

### 命令列表
![命令列表](./截图/screenshot_list.png)

### Nginx 状态
![Nginx 状态](./截图/screenshot_nginx_status.png)

### EC2 模拟
![EC2 模拟](./截图/screenshot_ec2.png)




\## 踩坑记录



\- `modules/` 目录下必须有 `\_\_init\_\_.py`（空文件即可），否则 Python 无法识别模块

\- `subprocess.run()` 调用外部脚本时，需确保脚本路径正确

\- 彩色输出依赖 `colorama` 库，未安装时会自动降级为普通输出



\## 后续计划



\- \[ ] 加入 Docker 容器化支持

\- \[ ] 添加真实 AWS 环境切换（非模拟）

\- \[ ] 增加 Terraform 资源管理模块

\- \[ ] 提供安装脚本（`setup.py` 或一键安装）



\## 总结



`cloud-toolkit` 是你从“学习命令”到“整合工具”的一次完整练习。它把所有手动操作、自动化脚本、模拟环境整合成一个可用的命令行工具，展示了模块化设计、命令行交互、错误处理等工程实践。



> 通过这个项目，你掌握了：

> -  Python 命令行工具开发

> -  模块化设计与代码复用

> -  Nginx 自动化部署流程

> -  AWS EC2 模拟管理（Boto3 + Moto）

> -  项目整合与交付能力



\## 相关项目



\- \[项目一：手动部署 Nginx](https://github.com/zhangbotao-2004/linux-web-deploy-practice)

\- \[项目二：Nginx 自动化部署](https://github.com/zhangbotao-2004/nginx-auto-deploy)

\- \[项目三：EC2 实例管理](https://github.com/zhangbotao-2004/ec2-manager)

\- \[项目四：综合管理工具](https://github.com/zhangbotao-2004/cloud-manager-tool)

