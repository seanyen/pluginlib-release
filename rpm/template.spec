Name:           ros-kinetic-pluginlib
Version:        1.10.2
Release:        0%{?dist}
Summary:        ROS pluginlib package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/pluginlib
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       ros-kinetic-class-loader
Requires:       ros-kinetic-rosconsole
Requires:       ros-kinetic-roslib >= 1.11.1
Requires:       tinyxml-devel
BuildRequires:  boost-devel
BuildRequires:  ros-kinetic-catkin >= 0.5.68
BuildRequires:  ros-kinetic-class-loader
BuildRequires:  ros-kinetic-cmake-modules
BuildRequires:  ros-kinetic-rosconsole
BuildRequires:  ros-kinetic-roslib >= 1.11.1
BuildRequires:  tinyxml-devel

%description
The pluginlib package provides tools for writing and dynamically loading plugins
using the ROS build infrastructure. To work, these tools require plugin
providers to register their plugins in the package.xml of their package.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Mon Mar 14 2016 Mikael Arguedas <mikael@osrfoundation.org> - 1.10.2-0
- Autogenerated by Bloom

