from setuptools import setup, find_packages

with open("requirements.txt", encoding="utf-8") as f:
    requirements = [line.strip() for line in f if line.strip() and not line.startswith("#")]

setup(
    name="ai-toolbox",
    version="1.0.0",
    description="AI 工具箱 - 命令行 AI 综合工具",
    author="AI Toolbox",
    packages=find_packages(),
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "ai=ai_toolbox.main:main",
        ],
    },
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)