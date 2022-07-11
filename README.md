# fedora-amdgpu-pro
A repository that provides the proprietary driver for fedora without having to deal with hassle of getting RHEL repo to work , and it has 32 bit libraries.

The end goal of this repository is to hand it over to glourious eggroll , so he can use it to supply AMD proprietary to nobara/fedora users


# Q&A

* Who's responsiable for this?


Some dumb 14 year old on the internet.


* Proprietary drivers on AMD? thought those guys were open source ??


While yes AMD driver stack is mostly open-source , some corporate greed still runs in the blood
as some parts remains proprietary like :


- The legacy/pal/orca OpenCL drivers. (required for darktable , resolve & blender (< 3.0) .)
- The industrial OpenGL drivers (required for resolve.)
- The Advanced Media Framework System Runtime 
- A Vulkan driver with ray tracing capabilities


# How to use

- install the binaries from the releases section or maybe a repo one day or learn to generate them on your own system

# For Vulkan

- install amdgpu-vulkan-switcher from https://copr.fedorainfracloud.org/coprs/gloriouseggroll/amdgpu-vulkan-switcher/
- make a symbolic from the actual vulkan icd to the place the switcher tries to read
- for amdvlk-pro 64 bit 
 ```
 sudo ln -s /opt/amdgpu-pro/etc/vulkan/icd.d/amd_icd64.json /usr/share/vulkan/icd.d/amd_pro_icd64.json 
 ```
 - for amdvlk-pro 32 bit
 ```
 sudo ln -s /opt/amdgpu-pro/etc/vulkan/icd.d/amd_icd32.json /usr/share/vulkan/icd.d/amd_pro_icd32.json

 ```
 - Now run the program with 
  ```
  vk_pro {THE_PROGRAM}
   ```
 
 
 - for amdvlk 64 bit 
 ```
 sudo ln -s /etc/vulkan/icd.d/amd_icd64.json /usr/share/vulkan/icd.d/amd_icd64.json
 ```
 - for amdvlk 32 bit
 ```
 sudo ln -s /etc/vulkan/icd.d/amd_icd32.json /usr/share/vulkan/icd.d/amd_icd32.json

 ```
 - Now run the program with 
  ```
  vk_amdvlk {THE_PROGRAM}
   ```

# For AMF

- Just run the program the needs AMF with vk_pro and it will work.

# For OpenCL

- The system will do what ends to do automatically .

# For OpenGL

~~install amdgpu-opengl-switcher from XYZ ~~
~~and run your program with~~
```
gl_pro {THE_PROGRAM}
```
**COMING SOON**

.

# How to manually compile 

Go into the tarball makers , each package will have 4 scripts , choose define the version of the driver you want in all 4 scripts (and your .spec file) , and run them by order , you will end up with a tar ball throw it in your rpm **BUILD** directory , and build the spec using the proper architecture (x86_64 or i686) , and enjoy!

.
