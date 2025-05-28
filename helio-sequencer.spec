%global juce_name JUCE
%global juce_commit 765814eab027d07171eabf2a5cd4fafd25cd2cdb
%global juce_shortcommit %(c=%{juce_commit}; echo ${c:0:7})

%global hopscotch_name Hopscotch-map
%global hopscotch_map_commit 9415490f2fb2a7127d2b72e5472c11dfc12f6463
%global hopscotch_map_shortcommit %(c=%{hopscotch_map_commit}; echo ${c:0:7})
Name:		helio-sequencer
Version:	3.16
Release:	1
Source0:	https://github.com/helio-fm/helio-sequencer/archive/refs/tags/%{version}.tar.gz
Source1:    https://github.com/helio-fm/JUCE/archive/%{juce_commit}/%{juce_name}-%{juce_shortcommit}.tar.gz
Source2:    https://github.com/Tessil/hopscotch-map/archive/%{hopscotch_map_commit}/%{hopscotch_name}-%{hopscotch_map_shortcommit}.tar.gz
Summary:	Libre music sequencer for desktop and mobile platform
URL:		https://github.com/helio-fm/helio-sequencer
License:	GPL-3.0
Group:		Application/Music
BuildRequires:	make
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	cmake(OpenShotAudio)
BuildRequires:	pkgconfig(xinerama)
BuildRequires:	pkgconfig(xrandr)
BuildRequires:	pkgconfig(jack)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(glx)
BuildRequires:	pkgconfig(xcursor)

%description
%summary.

%prep
%autosetup -p1
tar -xf %{S:1} -C %{builddir}/%{name}-%{version}/ThirdParty/%{juce_name} --strip-components=1
tar -xf %{S:2} -C %{builddir}/%{name}-%{version}/ThirdParty/HopscotchMap --strip-components=1

%build
%make_build -C Projects/LinuxMakefile/

%install
install -dm0775 %{buildroot}%{_bindir} %{buildroot}%{_iconsdir}/hicolor/256x256/apps %{buildroot}%{_datadir}/applications
install -Dm0775 Projects/LinuxMakefile/build/helio %{buildroot}%{_bindir}
install -Dvm644 Projects/Deployment/Linux/Debian/x64/usr/share/applications/Helio.desktop %{buildroot}%{_datadir}/applications/
install -Dvm644 Projects/Deployment/Linux/AppImage/x64/helio-workstation.png %{buildroot}%{_iconsdir}/hicolor/256x256/apps/

%files
%license LICENSE
%{_bindir}/helio
%{_datadir}/applications/Helio.desktop
%{_iconsdir}/hicolor/256x256/apps/helio-workstation.png
