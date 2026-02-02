# Minisoft Python API（miniapi）

> Minisoft Python API（miniapi）是一个库，可以让您的 Python 源代码在任何平台上顺利运行。使用它，您的 Python 源代码可以在任何平台上无需修改即可运行。
> **注意** 该项目目前处于早期开发阶段，其功能可能不稳定。

## 主要用途
- 为 Minisoft 软件或其他开发者的 Python 源代码提供跨平台兼容层。
- 可作为 Minisoft 软件或其他开发者开发的软件的插件 API 模板。

## 主要功能
- 文件操作
- 进程管理
- 网络访问
- 软件日志记录
- 性能监控
- 平台检测
......

## 使用方法
### 方法 1：作为 Python 库导入
> 首先，您需要从 GitHub 或 PyPI 获取 miniapi。
```bash or cmd
# PyPI
pip install miniapi
```
```bash or cmd
# GitHub
git clone https://github.com/Douglas-Woods2023/miniapi.git

pip install -e .
```
> 然后可以将其导入到您的 Python 源代码中。
```Python
import miniapi
```
### 方法 2：作为 Minisoft 软件插件 API 导入
- 详情请参考 [Minisoft Python API 文档](http://sj.frp.one:40092/miniapi.html)。

## 获取途径
1. [GitHub](https://github.com/Douglas-Woods2023/miniapi)
2. [PyPI](https://pypi.org/)
3. Minisoft 软件源代码中

## 许可
- MIT 许可