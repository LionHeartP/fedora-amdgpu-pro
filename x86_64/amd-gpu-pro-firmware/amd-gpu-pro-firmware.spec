%define _build_id_links none

# global info
%global repo 6.0.3
%global major 23.40
%global minor 1741713
# pkg info
%global amf 1.4.33
%global enc 1.0
%global amdvlk 2024.Q2.2
# drm info
%global drm 2.4.116.60003-1739731
%global amdgpu 1.0.0.60003-1739731
# firmware info
%global firmware_rev 6.3.6
%global firmware_maj 60003
%global firmware_min 1739731
%global _firmwarepath	/usr/lib/firmware
# Distro info
%global fedora 40
%global ubuntu 22.04

Name:     amd-gpu-pro-firmware
Version:  %{repo}
Release:  1%{?dist}
License:       AMDGPU PRO  EULA NON-REDISTRIBUTABLE
Group:         System Environment/Libraries
Summary:       System runtime for AMD Advanced Media Framework
URL:      http://repo.radeon.com/amdgpu

%undefine _disable_source_fetch
Source0:  http://repo.radeon.com/amdgpu/%{repo}/ubuntu/pool/main/a/amdgpu-dkms/amdgpu-dkms-firmware_%{firmware_rev}.%{firmware_maj}-%{firmware_min}.%{ubuntu}_all.deb

Provides: amd-gpu-firmware
Obsoletes: amd-gpu-firmware

BuildRequires: wget 
BuildRequires: cpio

Requires(post): /usr/bin/dracut 
Requires(postun): /usr/bin/dracut

%description
Firmware required for AMD AMF encoder support

%prep
mkdir -p files

ar x --output . %{SOURCE0}
tar -xJC files -f data.tar.xz || tar -xC files -f data.tar.gz

%install
mkdir -p %{buildroot}/usr/lib/firmware/amdgpu
cp -r files/usr/src/amdgpu-%{firmware_rev}-%{firmware_min}.%{ubuntu}/firmware/amdgpu/* %{buildroot}%{_firmwarepath}/amdgpu/ || true
cp -r files/lib/firmware/updates/amdgpu/* %{buildroot}%{_firmwarepath}/amdgpu/

%files
%{_firmwarepath}/amdgpu/

%post
/usr/bin/dracut -f

%postun
/usr/bin/dracut -f
