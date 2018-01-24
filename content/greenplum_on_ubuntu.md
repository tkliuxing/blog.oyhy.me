Date: 2018-01-24
Title: Greenplum 在 Ubuntu 上的安装与配置
Published: true
Type: post
Category: Coding
Tags: postgresql, greenplum, database, ubuntu
Slug: greenplum-on-ubuntu

## 安装

* 参考：[来源](http://greenplum.org/install-greenplum-oss-on-ubuntu/)

1. 添加 PPA： `sudo add-apt-repository ppa:greenplum/db`
2. 更新 APT 仓库： `sudo apt-get update`
3. 安装： `sudo apt-get install greenplum-db-oss`

安装之后，会在`/opt/gpdb`目录中添加所有 greenplum 的依赖以及工具。

### 初始化环境

1. 在shell中执行 `. /opt/gpdb/greenplum_path.sh`，或添加到 `~/.bashrc` 中。
2. 拷贝基础配置到项目目录：`cp $GPHOME/docs/cli_help/gpconfigs/gpinitsystem_singlenode .`
3. 编辑此文件：
~~~~.shell
# 创建此文件并写入当前主机名
MACHINE_LIST_FILE=./hostlist_singlenode

# 编辑以下这行，指定数据目录，并确保目录已经存在，如：
declare -a DATA_DIRECTORY=(/gpdata1 /gpdata2)
declare -a DATA_DIRECTORY=(/home/inovick/primary /home/inovick/primary)

# 修改下面这行，更换为当前主机名
MASTER_HOSTNAME=hostname_of_machine
MASTER_HOSTNAME=ubuntu

# 修改下面这行，指定 master 数据目录，并确保目录已存在
MASTER_DIRECTORY=/home/inovick/master
~~~~
4. 初始化数据库连接配置：`gpssh-exkeys -f hostlist_singlenode`
5. 初始化数据库： `gpinitsystem -c gpinitsystem_singlenode`

以上步骤完成后，数据库就已经启动了，但是在下次启动的时候需要配置环境变量 `MASTER_DATA_DIRECTORY`,
此变量需要指向配置文件中 `MASTER_DIRECTORY` 目录下的 `gpsne-1` 目录。

## 配置greenplum

greenplum master的配置文件保存在 `MASTER_DIRECTORY` 目录下的 `gpsne-1` 目录，
包含 postgresql 的相关配置如： `pg_hba.conf`, `postgresql.conf` 等。

编辑相关配置后需要重新reload，reload命令： `gpstop -u`。

* 启动 master 为维护模式，只有管理员可登录： `gpstart -m`
* 维护终端连接方式：`PGOPTIONS='-c gp_session_role=utility' psql postgres`
* 完成维护后恢复为生产模式： `gpstop -mr`

### 停止greenplum服务

使用 `gpstop` 命令




