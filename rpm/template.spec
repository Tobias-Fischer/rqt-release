Name:           ros-kinetic-rqt-gui
Version:        0.3.1
Release:        0%{?dist}
Summary:        ROS rqt_gui package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/rqt_gui
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-catkin
Requires:       ros-kinetic-qt-gui >= 0.3.0
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-qt-gui >= 0.3.0

%description
rqt_gui provides the main to start an instance of the ROS integrated graphical
user interface provided by qt_gui.

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
* Fri Apr 01 2016 Dirk Thomas <dthomas@osrfoundation.org> - 0.3.1-0
- Autogenerated by Bloom

* Fri Apr 01 2016 Dirk Thomas <dthomas@osrfoundation.org> - 0.3.0-0
- Autogenerated by Bloom

