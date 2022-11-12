from setuptools import Extension, setup

setup(
    ext_modules=[
        Extension(
            name="cython_package_build_example.main",
            sources=["src/cython_package_build_example/main.pyx"],
        ),
    ]
)
