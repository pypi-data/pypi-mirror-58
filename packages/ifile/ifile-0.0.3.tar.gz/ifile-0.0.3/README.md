# YFile

各组件版本：
```
ansible==2.8.1
```

各节点IP：
```bash
10.211.55.5
10.211.55.6
10.211.55.7
```

其中10.211.55.5既是管理节点，又是子节点

## 初始化环境
```bash
yum install epel-release -y
yum install python-pip -y
yum install docker -y
```

```bash
pip install docker-compose
```

安装docker依赖包, 当使用ansible的docker-container模块时使用
```bash
pip install docker
```

### 初始化管理节点
#### 安装依赖
```bash
yum install git ansible -y
```

#### 创建docker私有仓库
配置docker。编辑/etc/docker/daemon.json，内容如下：
```bash
{
    "hosts": ["tcp://0.0.0.0:2375", "unix:///var/run/docker.sock"],
    "insecure-registries":["10.211.55.5:6666"]
}
```

hosts参数是为了能够远程连接管理docker，如使用portainer工具（参考[docker-images](https://github.com/Glf9832/docker-images)中的文档）；
insecure-registries参数是为了使registry不需要使用https。

***注意：*** 子节点也需要配置此项！

重启docker
```bash
systemctl restart docker
```

运行registry容器
```bash
docker run -d -p 6666:5000 --restart always --name registry registry:2.7.1
```

以redis镜像为例，推送镜像至我们的私有仓库以及从仓库拉取镜像：

```bash
docker tag redis:4.0.14 10.211.55.5:6666/redis:4.0.14
docker push 10.211.55.5:6666/redis:4.0.14
```

```bash
docker pull 10.211.55.5:6666/redis:4.0.14
```

## 应用部署

应用中用到的环境变量如下：
```
tm_env='DEV'
tm_web_port='8000'
tm_redis_host='localhost'
tm_redis_port='6379'
```

### 创建Docker镜像
```bash
docker pull redis:4.0.14
docker build -f deploy/docker/Dockerfile.base -t app-base:latest .
docker build -f deploy/docker/Dockerfile -t yfile-app:latest .
```

设置标签
```bash
docker tag redis:4.0.14 10.211.55.5:6666/redis:4.0.14
docker tag cnas-base:latest 10.211.55.5:6666/app-base:latest
docker tag cnas-app:latest 10.211.55.5:6666/cnas-app:latest
```

推送镜像至私有仓库
```bash
docker push 10.211.55.5:6666/redis:4.0.14
docker push 10.211.55.5:6666/app-base:latest
docker push 10.211.55.5:6666/cnas-app:latest
```

### Docker-compose管理应用
```bash
docker-compose -f deploy/docker/docker-compose.yaml up
docker-compose -f deploy/docker/docker-compose.yaml stop
docker-compose -f deploy/docker/docker-compose.yaml rm
```

## ansible管理节点的配置 

### 创建ssh公钥，免密登录
```bash
ssh-keygen
```

为管理节点的公钥到每个子节点的authorized_keys
```bash
ssh-copy-id user@host
```

### 拉取源代码

```bash
git clone https://github.com/Glf9832/timemachine_example.git
```

### ansible部署docker容器
初始化节点
```bash
ansible-playbook -i hosts deploy/ansible/init.yaml
```

启动容器
```bash
ansible-playbook -i hosts deploy/ansible/service.yaml
```

### 创建数据库

mysql 5.7
```bash
grant all privileges on yfile.* to 'yfile'@'%' identified by 'password' with grant option;
```

mysql 8.0
```
CREATE USER 'ifile'@'%' IDENTIFIED BY '123456';
GRANT ALL PRIVILEGES ON ifile.* TO 'ifile'@'%' WITH GRANT OPTION;
flush privileges;
```

```
drop user ifile@'%';
```

### 版本发布流程
在用户主目录下设置 *.pypirc* , 如下：
```vim
[distutils]
index-servers = pypi

[pypi]
username: example_user
password: example_password
```

安装版本发布工具
```bash
pip3 install setuptools wheel twine
```

发布版本到pypi，仓库地址是https://test.pypi.org/legacy/
```bash
python3 setup.py sdist bdist_wheel
twine upload dist/*
```

## TODO
1. 代码整理，梳理业务流程;
2. flask的send_file实现文件下载功能;
3. docker脚本更新，自动化部署;
4. 计算文件实际size，更新配置库;
5. pytest单元测试;
6. travis集成测试;
7. tox集成;
8. 配置库及GridFS文件清理命令行，仅供开发调试使用; DONE
9. 日志记录功能;
10. sentry代码监控;
11. 新增图片类别的关系表;
12. 项目名称调整;
13. 添加文件原始路径字段;
14. 数据库表中文件名需要支持中文;
15. 管理员的配置库管理（链接串等）
