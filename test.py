"""
Miniapi 快速开始示例
"""
import miniapi
from miniapi import timer
import logging
import time
import tkinter as tk

# 1. 平台信息
print(f"平台: {miniapi.platform_name()}")
print(f"是否是Windows: {miniapi.IS_WINDOWS}")
print(f"是否是Linux: {miniapi.IS_LINUX}")

# 2. 文件操作
print("\n--- 文件操作示例 ---")

# 创建测试目录
test_dir = miniapi.mkdir("./test_miniapi")
print(f"创建目录: {test_dir}")

# 创建测试文件
(test_dir / "hello.txt").write_text("Hello Miniapi!")

# 复制文件
miniapi.cp(test_dir / "hello.txt", test_dir / "hello_copy.txt")
print("文件复制完成")

# 查找文件
files = miniapi.find_files("*.txt", test_dir)
print(f"找到文件: {files}")

# 删除文件
miniapi.rm(test_dir / "hello_copy.txt")
print("文件删除完成")

# 3. 进程管理
print("\n--- 进程管理示例 ---")

# 安全执行命令
result = miniapi.run(["python", "--version"])
#result = miniapi.run("python3 --version")
print(f"Python版本: {result.stdout}")

# 快速捕获输出
output = miniapi.sh(["echo", "Hello from Miniapi!"])
print(f"命令输出: {output}")

# 4. 性能监控
print("\n--- 性能监控示例 ---")

@timer("批量操作")
def batch_operations():
    # 批量创建文件
    for i in range(10):
        (test_dir / f"file_{i}.txt").write_text(f"Content {i}")
    
    # 批量查找
    files = miniapi.find_files("*.txt", test_dir)
    print(f"创建了 {len(files)} 个文件")
    
    # 批量删除
    #time.sleep(30)
    miniapi.bulk_remove([test_dir / f"file_{i}.txt" for i in range(10)])

batch_operations()


# 5. 日志记录
print("\n--- 日志记录 ---")
test_logger = miniapi.setup_logger(log_file="./miniapi.log", use_colors=True, level=logging.DEBUG)
test_logger.debug("This is a debug message.")
test_logger.info("This is an info message.")
test_logger.warning("This is a warning message.")
test_logger.error("This is an error message.")
test_logger.critical("This is a critical message.")
test_logger.info("This is a logging test from Miniapi.")

# 6. 网络操作
print("\n--- 网络操作 ---")
ret = miniapi.fetch("https://github.com", method="GET", timeout=5, headers={"User-Agent": "Miniapi-Test"}, data=None)
test_logger.debug(f"Fetched GitHub homepage.Returned status code: {ret.status_code}")

miniapi.download("http://192.168.1.128/9.PNG", "./example.png", params=None)
test_logger.info("Downloaded example.png from local server.")

ret = miniapi.upload("http://192.168.1.128/Linux/Users/Douglas/test.php", "./test.txt", data={"key": "value"})
test_logger.debug(f"Uploaded test.txt.Returned status code: {ret.status_code}")

ret = miniapi.tqdm_download("http://192.168.1.128/game_3.0.0.apk", "./example_tqdm.apk", params=None)
test_logger.debug(f"Tqdm download completed.Returned status code: {ret.status_code}")

root = tk.Tk()
root.geometry("300x100")
root.title("Miniapi GUI下载示例")
def download_test():
    miniapi.GUI_download("http://192.168.1.128/Dev-Cpp_4.9.2_Setup.exe", "./example_gui.exe", params=None, parent=root)
    test_logger.info("GUI download completed.")
tk.Button(root, text="开始GUI下载", command=download_test).pack()
tk.Button(root, text="退出", command=root.destroy).pack()
root.mainloop()

# 7. 清理
print("\n--- 清理 ---")
miniapi.rm("./example.png")
miniapi.rm("./example_tqdm.apk")
miniapi.rm("./example_gui.exe")
miniapi.rm(test_dir, recursive=True)
test_logger.info("Cleanup completed.")

test_logger.info("✅ Miniapi example completed!")