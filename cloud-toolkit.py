#!/usr/bin/env python3
"""
cloud-toolkit.py - 云服务管理工具

用法:
  python3 cloud-toolkit.py nginx         # 完整部署 Nginx
  python3 cloud-toolkit.py nginx-status  # 查看 Nginx 状态
  python3 cloud-toolkit.py ec2           # 运行 EC2 模拟
  python3 cloud-toolkit.py menu          # 交互式菜单
  python3 cloud-toolkit.py list          # 列出所有可用命令
  python3 cloud-toolkit.py help          # 显示本帮助
"""

import sys
import subprocess
import os
from datetime import datetime

# 颜色输出（可选，如果 colorama 未安装则降级）
try:
    from colorama import init, Fore, Style
    init(autoreset=True)
    GREEN = Fore.GREEN
    RED = Fore.RED
    YELLOW = Fore.YELLOW
    BLUE = Fore.BLUE
    BOLD = Style.BRIGHT
    RESET = Style.RESET_ALL
except ImportError:
    # 降级方案：无颜色
    GREEN = RED = YELLOW = BLUE = BOLD = RESET = ""

# 模块路径（假设 nginx_manager.py 和 ec2_manager.py 在同一目录）
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
NGINX_MODULE = os.path.join(BASE_DIR, "nginx_manager.py")
EC2_MODULE = os.path.join(BASE_DIR, "ec2_manager.py")

def print_header(title):
    """打印带装饰的标题"""
    print(f"\n{BOLD}{BLUE}╔{'═' * 50}╗{RESET}")
    print(f"{BOLD}{BLUE}║ {title.center(48)} ║{RESET}")
    print(f"{BOLD}{BLUE}╚{'═' * 50}╝{RESET}\n")

def print_success(msg):
    print(f"{GREEN}✅ {msg}{RESET}")

def print_error(msg):
    print(f"{RED}❌ {msg}{RESET}")

def print_info(msg):
    print(f"{YELLOW}ℹ️  {msg}{RESET}")

def run_script(script_path, args=None):
    """安全运行子脚本"""
    if not os.path.exists(script_path):
        print_error(f"模块不存在: {script_path}")
        print_info("请确保 nginx_manager.py 和 ec2_manager.py 在同一目录下")
        return False
    
    cmd = ["python3", script_path]
    if args:
        cmd.append(args)
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0:
            print(result.stdout)
            return True
        else:
            print_error(f"执行失败 (返回码: {result.returncode})")
            if result.stderr:
                print(result.stderr)
            return False
    except Exception as e:
        print_error(f"执行异常: {e}")
        return False

def cmd_nginx():
    """完整部署 Nginx"""
    print_header("Nginx 完整部署")
    run_script(NGINX_MODULE, "full")

def cmd_nginx_status():
    """查看 Nginx 状态"""
    print_header("Nginx 服务状态")
    run_script(NGINX_MODULE, "status")

def cmd_ec2():
    """运行 EC2 模拟"""
    print_header("EC2 实例管理模拟")
    run_script(EC2_MODULE, "mock")

def cmd_menu():
    """交互式菜单（调用原 main.py）"""
    print_header("交互式菜单")
    # 尝试调用项目四的 main.py
    main_py = os.path.join(BASE_DIR, "main.py")
    if os.path.exists(main_py):
        run_script(main_py)
    else:
        print_info("main.py 不存在，使用简易菜单:")
        while True:
            print("\n1. 部署 Nginx")
            print("2. 查看 Nginx 状态")
            print("3. 运行 EC2 模拟")
            print("4. 退出")
            choice = input("请选择 (1-4): ").strip()
            if choice == "1":
                cmd_nginx()
            elif choice == "2":
                cmd_nginx_status()
            elif choice == "3":
                cmd_ec2()
            elif choice == "4":
                print_success("再见！")
                break
            else:
                print_error("无效选择，请重新输入")

def cmd_list():
    """列出所有可用命令"""
    print_header("可用命令")
    commands = [
        ("nginx", "完整部署 Nginx (安装 + 配置 + 验证)"),
        ("nginx-status", "查看 Nginx 服务状态"),
        ("ec2", "运行 EC2 模拟 (创建/停止/启动)"),
        ("menu", "交互式菜单"),
        ("list", "列出所有命令"),
        ("help", "显示帮助信息"),
    ]
    for cmd, desc in commands:
        print(f"  {BOLD}{cmd:15}{RESET} {desc}")
    print(f"\n{GREEN}共 {len(commands)} 个命令{RESET}")

def show_help():
    """显示帮助信息"""
    print_header("云服务管理工具 (Cloud Toolkit)")
    print("""
一个整合了 Nginx 自动化部署和 EC2 实例管理的命令行工具。

用法:
  python3 cloud-toolkit.py <命令>

命令列表:
  nginx          完整部署 Nginx（安装 + 改端口 80→8080 + 验证）
  nginx-status   查看 Nginx 服务状态
  ec2            运行 EC2 实例管理模拟（创建 → 停止 → 启动）
  menu           交互式菜单（适合不熟悉命令的用户）
  list           列出所有可用命令
  help           显示此帮助信息

示例:
  python3 cloud-toolkit.py nginx
  python3 cloud-toolkit.py nginx-status
  python3 cloud-toolkit.py ec2
  python3 cloud-toolkit.py menu
  python3 cloud-toolkit.py list
""")
    print_info(f"当前目录: {BASE_DIR}")
    print_info(f"Nginx 模块: {'✅ 存在' if os.path.exists(NGINX_MODULE) else '❌ 缺失'}")
    print_info(f"EC2 模块: {'✅ 存在' if os.path.exists(EC2_MODULE) else '❌ 缺失'}")

def main():
    if len(sys.argv) < 2:
        show_help()
        sys.exit(0)
    
    action = sys.argv[1]
    
    # 命令映射表
    commands = {
        "nginx": cmd_nginx,
        "nginx-status": cmd_nginx_status,
        "ec2": cmd_ec2,
        "menu": cmd_menu,
        "list": cmd_list,
        "help": show_help,
    }
    
    if action in commands:
        commands[action]()
    else:
        print_error(f"未知命令: {action}")
        print_info("输入 'help' 查看所有可用命令")
        sys.exit(1)

if __name__ == "__main__":
    main()