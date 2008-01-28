%define	name	gnome-sharp2
%define oname gnome-sharp
%define version 2.19.90
%define release %mkrel 2
%define mono 1.0.2
%define gtk_sharp 2.11.0
%define monodir %_prefix/lib/mono

Summary:	C# language binding for GNOME
Name:		%name
Version:	%version
Release:	%release
License:	LGPL
Group:		System/Libraries
URL:		http://gtk-sharp.sourceforge.net/
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/gnome-sharp/%oname-%version.tar.bz2
#gw svn fix for https://bugzilla.novell.com/show_bug.cgi?id=356649
Patch: gnome-sharp-94153-gnomeglobal.patch
BuildRoot:	%_tmppath/%name-buildroot
BuildRequires:	mono-devel >= %mono
BuildRequires:	libglade2.0-devel
BuildRequires:	libxslt-devel
BuildRequires:	libgnomeui2-devel
BuildRequires:	libgnomeprintui-devel
BuildRequires:	libGConf2-devel
BuildRequires:	gnome-panel-devel
BuildRequires:	gtk-sharp2-devel >= %{gtk_sharp}
BuildRequires:	gtk-sharp2 >= %{gtk_sharp}
BuildRequires:	glade-sharp2 >= %{gtk_sharp}

%description
Gtk-sharp is a C# language binding for GNOME.


%prep
rm -rf %buildroot

%setup -q -n %oname-%version
%patch -p0

%build
%configure2_5x
make

%install
rm -rf %buildroot
%makeinstall

rm -rf %buildroot%_libdir/lib*a

%clean
rm -rf %buildroot


%files
%defattr(-,root,root)
%doc ChangeLog README
%doc sample
%_bindir/gconfsharp2-schemagen
/usr/lib/gtk-sharp-2.0/gconfsharp-schemagen.exe
%monodir/gac/*art-sharp
%monodir/gtk-sharp-2.0/*art-sharp.dll*
%_libdir/pkgconfig/art-sharp-2.0.pc
%monodir/gac/*gconf-sharp
%monodir/gac/*gconf-sharp-peditors
%monodir/gac/*gnome-sharp
%monodir/gac/*gnome-vfs-sharp
%monodir/gtk-sharp-2.0/*gconf-sharp.dll*
%monodir/gtk-sharp-2.0/*gconf-sharp-peditors.dll*
%monodir/gtk-sharp-2.0/*gnome-sharp.dll*
%monodir/gtk-sharp-2.0/*gnome-vfs-sharp.dll*
%_libdir/pkgconfig/gconf-sharp-2.0.pc
%_libdir/pkgconfig/gconf-sharp-peditors-2.0.pc
%_libdir/pkgconfig/gnome-vfs-sharp-2.0.pc
%_libdir/pkgconfig/gnome-sharp-2.0.pc
%_libdir/libgnomesharpglue-2.so
%_datadir/gapi-2.0/*.xml
