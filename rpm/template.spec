Name:           ros-jade-rqt-gui-cpp
Version:        0.2.14
Release:        0%{?dist}
Summary:        ROS rqt_gui_cpp package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/rqt_gui_cpp
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-jade-nodelet
Requires:       ros-jade-qt-gui >= 0.2.22
Requires:       ros-jade-qt-gui-cpp >= 0.2.22
Requires:       ros-jade-roscpp
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-nodelet
BuildRequires:  ros-jade-qt-gui >= 0.2.22
BuildRequires:  ros-jade-qt-gui-cpp >= 0.2.22
BuildRequires:  ros-jade-roscpp

%description
rqt_gui_cpp enables GUI plugins to use the C++ client library for ROS.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Wed Apr 29 2015 Dirk Thomas <dthomas@osrfoundation.org> - 0.2.14-0
- Autogenerated by Bloom

