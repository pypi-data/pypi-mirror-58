from setuptools import setup, find_packages

setup(
    name='aws_codestar_cdk',
    version='1.0.2',
    license='GNU GENERAL PUBLIC LICENSE Version 3',
    packages=find_packages(exclude=['venv', 'test']),
    description='AWS CDK package that helps deploying a lambda function into CodeStar.',
    include_package_data=True,
    install_requires=[
        'aws_cdk.core',
        'aws_cdk.aws_iam',
        'aws_cdk.custom_resources',
        'aws_cdk.aws_s3',
        'aws_cdk.aws_s3_deployment'
    ],
    author='Deividas Tamkus, Laimonas Sutkus',
    author_email='dtamkus@gmail.com, laimonas.sutkus@gmail.com',
    keywords='AWS CDK CodeStar',
    url='https://github.com/laimonassutkus/AwsCodeStar.git',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)
