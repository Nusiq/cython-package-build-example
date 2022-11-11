from setuptools import Extension, setup

setup(
    ext_modules=[
        Extension(
            name="cython_lib_test.main",
            sources=["src/cython_lib_test/main.pyx"],
        ),
    ]
)
