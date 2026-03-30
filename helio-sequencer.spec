#global juce_name JUCE
#global juce_commit 765814eab027d07171eabf2a5cd4fafd25cd2cdb
#global juce_shortcommit %%(c=%%{juce_commit}; echo ${c:0:7})

#global hopscotch_name Hopscotch-map
#global hopscotch_map_commit 9415490f2fb2a7127d2b72e5472c11dfc12f6463
#global hopscotch_map_shortcommit %%(c=%%{hopscotch_map_commit}; echo ${c:0:7})

Summary:		Libre music sequencer for desktop and mobile platform
Name:	helio-sequencer
Version:		3.17
Release:		1
License:		GPLv3+
Group:	Sound
Url:		https://github.com/helio-fm/helio-sequencer
#Source0:	https://github.com/helio-fm/helio-sequencer/archive/refs/tags/%%{version}.tar.gz
# Submodules are a pain...
Source0:	%{name}-%{version}.tar.xz
BuildRequires:	cmake
BuildRequires:	make
BuildRequires:	cmake(OpenShotAudio)
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(glx)
BuildRequires:	pkgconfig(jack)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(xcursor)
BuildRequires:	pkgconfig(xinerama)
BuildRequires:	pkgconfig(xrandr)

%description
Libre music sequencer for desktop and mobile platform. It aims to be a modern
music creation software, featuring linear-based/pattern-based sequencer with
clean UI, integrated version control, microtonal temperaments support, small
portable builds and more; mainly targeted at hobbyist composers, game
developers and indie artists.

%files
%license LICENSE
%doc CHANGELOG.md README.md
%{_bindir}/helio
%{_datadir}/applications/Helio.desktop
%{_datadir}/metainfo/fm.helio.Workstation.metainfo.xml
%{_iconsdir}/hicolor/*/apps/helio-workstation.png

#-----------------------------------------------------------------------------

%prep
%autosetup -p1


%build
%make_build -C Projects/LinuxMakefile/


%install
# No automated install in makefile: go manually
install -dm0775 %{buildroot}%{_bindir} %{buildroot}%{_iconsdir}/hicolor/256x256/apps %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/metainfo
install -Dm0775 Projects/LinuxMakefile/build/helio %{buildroot}%{_bindir}
install -Dvm644 Projects/Deployment/Linux/Debian/x64/usr/share/applications/Helio.desktop %{buildroot}%{_datadir}/applications/
install -Dvm644 Projects/Deployment/Linux/AppImage/x64/helio-workstation.png %{buildroot}%{_iconsdir}/hicolor//256x256/apps/
install -Dvm644 Projects/Deployment/Linux/fm.helio.Workstation.metainfo.xml %{buildroot}%{_datadir}/metainfo/

# Fix perms
chmod 0755 %{buildroot}%{_bindir}/helio
