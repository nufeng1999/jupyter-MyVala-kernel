from ipykernel.kernelapp import IPKernelApp
from .kernel import MyValaKernel
IPKernelApp.launch_instance(kernel_class=MyValaKernel)
