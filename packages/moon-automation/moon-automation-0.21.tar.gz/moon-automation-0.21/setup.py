import os
from distutils.core import setup

module_dirs = os.listdir(os.path.join("moon_automation","Modules"))
modules = ['moon_automation','moon_automation.DeviceTypes','moon_automation.Modules']
package_data = {}
package_data["moon_automation"]=["*.yaml"]
for module in module_dirs:
  if os.path.isdir(os.path.join("moon_automation","Modules", module)) and "__" not in module:
    modules.append("moon_automation.Modules."+module)
    package_data["moon_automation"].append(os.path.join("Modules", module,"*.yaml"))
setup(
  name = 'moon-automation',         # How you named your package folder (MyLib)
  packages = modules,   # Chose the same as "name"
  version = '0.21',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'A automation framework to simplify automation tasks',   # Give a short description about your library
  author = 'Jiaming Li',                   # Type in your name
  author_email = 'jiaminli@cisco.com',      # Type in your E-Mail
  url = 'https://wwwin-github.cisco.com/jiaminli/moon',   # Provide either the link to your github or to your website
  download_url = 'https://wwwin-github.cisco.com/jiaminli/moon/archive/v0.21.tar.gz',    # I explain this later on
  keywords = ['AUTOMATION', 'CISCO'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'pyyaml',
          'pexpect',
          'jinja2'
      ],
  scripts=['sbin/moon','sbin/moon-init'],
  classifiers=[
    'Development Status :: 4 - Beta',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Libraries',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
  package_data = package_data
)
