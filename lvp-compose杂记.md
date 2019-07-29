# lvp-compose杂记

## 大致背景需求

对lvp项目（内部的轻量级虚拟化管理平台）提供docker-compose的的支持。

## 初步规划

保留核心的解析docker-compose.yml文件的功能，整合lvp与docker-compose中创建容器实例的功能，实现容器的统一创建，启动，停止，重启，删除等完整的生命周期管理。

## 开发计划

TODO:

1. 理解docker-compose代码
    docker-compose:
        
2. 精简docker-compose代码，保留核心功能
3. 与lvp进行整合
    1. docker-compose文件内容解析，标准化入库
    2. docker container启动方式的标准换化处理，与lvp统一
        1. run
        2. create
        3. start 
        4. stop 
        5. remove
        6. ...


## 其它


