import sys
import os

def install_nginx():
    print("更新软件列表...")
    os.system("sudo apt update")
    print("安装 Nginx...")
    os.system("sudo apt install nginx -y")
    print("✅ Nginx 安装完成")

def check_status():
    print("查看 Nginx 服务状态：")
    os.system("sudo systemctl status nginx --no-pager")

def restart_nginx():
    print("重启 Nginx...")
    os.system("sudo systemctl restart nginx")
    print("✅ Nginx 已重启")

def test_nginx():
    print("测试配置文件语法...")
    os.system("sudo nginx -t")

def full_deploy():
    print("\n🚀 开始自动化部署 Nginx...\n")
    install_nginx()
    check_status()
    print("修改配置文件（80 → 8080）...")
    os.system("sudo sed -i 's/listen 80;/listen 8080;/g' /etc/nginx/sites-available/default")
    os.system("sudo sed -i 's/listen [::]:80;/listen [::]:8080;/g' /etc/nginx/sites-available/default")
    test_nginx()
    restart_nginx()
    print("验证端口监听（8080）：")
    os.system("sudo ss -tunlp | grep 8080")
    print("本地访问测试：")
    os.system("curl -s http://localhost:8080 | head -5")
    print("✅ Nginx 自动化部署完成！")

def show_help():
    print("用法: python3 nginx_manager.py [选项]")
    print("  full      - 完整部署流程")
    print("  install   - 仅安装 Nginx")
    print("  status    - 查看状态")
    print("  restart   - 重启服务")
    print("  test      - 测试配置语法")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        show_help()
        sys.exit(0)
    
    action = sys.argv[1]
    if action == "full":
        full_deploy()
    elif action == "install":
        install_nginx()
    elif action == "status":
        check_status()
    elif action == "restart":
        restart_nginx()
    elif action == "test":
        test_nginx()
    else:
        show_help()