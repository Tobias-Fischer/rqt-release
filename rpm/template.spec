Name:           ros-lunar-rqt
Version:        0.5.0
Release:        0%{?dist}
Summary:        ROS rqt package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/rqt
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-lunar-rqt-gui >= 0.3.0
Requires:       ros-lunar-rqt-gui-cpp >= 0.3.0
Requires:       ros-lunar-rqt-gui-py >= 0.3.0
BuildRequires:  ros-lunar-catkin

%description
rqt is a Qt-based framework for GUI development for ROS. It consists of three
parts/metapackages rqt (you're here) rqt_common_plugins - ROS backend tools
suite that can be used on/off of robot runtime. rqt_robot_plugins - Tools for
interacting with robots during their runtime. rqt metapackage provides a widget
rqt_gui that enables multiple `rqt` widgets to be docked in a single window.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/lunar" \
        -DCMAKE_PREFIX_PATH="/opt/ros/lunar" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/lunar

%changelog
* Mon Apr 24 2017 Dirk Thomas <dthomas@osrfoundation.org> - 0.5.0-0
- Autogenerated by Bloom

* Fri Feb 24 2017 Dirk Thomas <dthomas@osrfoundation.org> - 0.3.2-0
- Autogenerated by Bloom

