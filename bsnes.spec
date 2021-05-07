Name:           bsnes
Version:        master
Release:        %{?dist}
Summary:        Super NES emulator
Group:          System/Emulators/Other
License:        GPLv3
#URL:            
%undefine _disable_source_fetch
Source0:        https://github.com/bsnes-emu/bsnes/archive/refs/heads/master.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  gtk2-devel SDL2-devel libXv-devel pulseaudio-libs-devel alsa-lib-devel systemd-devel
Requires:       gtk2 SDL2 pulseaudio-libs alsa-lib

%description


%prep
%setup -q -n bsnes-master

%build
hiro=gtk2 make -C bsnes %{?_smp_mflags}


%install
make prefix=%{buildroot}%{_prefix} -C bsnes install

%clean
rm -rf $RPM_BUILD_ROOT


%files
%{_bindir}/%{name}*
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/256x256/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

%doc

%changelog