%define	name	gnome-sharp2
%define oname gnome-sharp
%define version 2.24.2
%define release %mkrel 4
%define mono 1.0.2
%define gtk_sharp 2.12.1
%define monodir %_prefix/lib/mono

Summary:	C# language binding for GNOME
Name:		%name
Version:	%version
Release:	%release
License:	LGPLv2
Group:		System/Libraries
URL:		http://gtk-sharp.sourceforge.net/
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/gnome-sharp/%oname-%version.tar.bz2
BuildRoot:	%_tmppath/%name-buildroot
BuildRequires:	mono-devel >= %mono
BuildRequires:	libglade2.0-devel
BuildRequires:	libxslt-devel
BuildRequires:	libgnomeui2-devel
BuildRequires:	libgnomeprintui-devel
BuildRequires:	libGConf2-devel
BuildRequires:	libpanel-applet-2-devel
BuildRequires:	gtk-sharp2-devel >= %{gtk_sharp}
BuildRequires:	gtk-sharp2 >= %{gtk_sharp}
BuildRequires:	glade-sharp2 >= %{gtk_sharp}

%description
This is a C# language binding for GNOME.

%package 2.4
Summary: C# language binding for GNOME 2.4
Group: System/Libraries
Requires: %{name} = %version
Conflicts: %{name} < 2.24.2-3

%description 2.4
This is a C# language binding for GNOME 2.4.

%package 2.6
Summary: C# language binding for GNOME 2.6
Group: System/Libraries
Requires: %{name} = %version
Conflicts: %{name} < 2.24.2-3

%description 2.6
This is a C# language binding for GNOME 2.6.

%package 2.8
Summary: C# language binding for GNOME 2.8
Group: System/Libraries
Requires: %{name} = %version
Conflicts: %{name} < 2.24.2-3

%description 2.8
This is a C# language binding for GNOME 2.8.

%package 2.16
Summary: C# language binding for GNOME 2.16
Group: System/Libraries
Requires: %{name} = %version
Conflicts: %{name} < 2.24.2-3

%description 2.16
This is a C# language binding for GNOME 2.16.

%package 2.20
Summary: C# language binding for GNOME 2.20
Group: System/Libraries
Requires: %{name} = %version
Conflicts: %{name} < 2.24.2-3

%description 2.20
This is a C# language binding for GNOME 2.20.

%package devel
Summary: C# language binding for GNOME - devel files
Group: Development/Other
Requires: %name = %version
Requires: gtk-sharp2-devel

%description devel
This is a C# language binding for GNOME. It contains all files that are needed
to build against %{name}.

%prep
%setup -qn %oname-%version

%build
%configure2_5x
make

%install
rm -rf %buildroot
%makeinstall_std

rm -rf %buildroot%_libdir/lib*a

%clean
rm -rf %buildroot


%files
%defattr(-,root,root)
%doc README
%{_libdir}/libgnomesharpglue-2.so
%monodir/gtk-sharp-2.0/art-sharp.dll
%monodir/gtk-sharp-2.0/gconf-sharp-peditors.dll
%monodir/gtk-sharp-2.0/gconf-sharp.dll
%monodir/gtk-sharp-2.0/gnome-sharp.dll
%monodir/gtk-sharp-2.0/gnome-vfs-sharp.dll
%monodir/gac/art-sharp/2.24.0.0*
%monodir/gac/gconf-sharp-peditors/2.24.0.0*
%monodir/gac/gconf-sharp/2.24.0.0*
%monodir/gac/gnome-sharp/2.24.0.0*
%monodir/gac/gnome-vfs-sharp/2.24.0.0*

%files 2.4
%defattr(-,root,root)
%monodir/gtk-sharp-2.0/policy.2.4.*.dll
%monodir/gac/policy.2.4.*

%files 2.6
%defattr(-,root,root)
%monodir/gtk-sharp-2.0/policy.2.6.*.dll
%monodir/gac/policy.2.6.*

%files 2.8
%defattr(-,root,root)
%monodir/gtk-sharp-2.0/policy.2.8.*.dll
%monodir/gac/policy.2.8.*

%files 2.16
%defattr(-,root,root)
%monodir/gtk-sharp-2.0/policy.2.16.*.dll
%monodir/gac/policy.2.16.*

%files 2.20
%defattr(-,root,root)
%monodir/gtk-sharp-2.0/policy.2.20.*.dll
%monodir/gac/policy.2.20.*

%files devel
%defattr(-,root,root)
%doc ChangeLog
%doc sample
%_bindir/gconfsharp2-schemagen
%_prefix/lib/gtk-sharp-2.0/gconfsharp-schemagen.exe
%_datadir/gapi-2.0/*.xml
%_libdir/pkgconfig/art-sharp-2.0.pc
%_libdir/pkgconfig/gconf-sharp-2.0.pc
%_libdir/pkgconfig/gconf-sharp-peditors-2.0.pc
%_libdir/pkgconfig/gnome-vfs-sharp-2.0.pc
%_libdir/pkgconfig/gnome-sharp-2.0.pc
