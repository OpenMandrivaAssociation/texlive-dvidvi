# revision 26689
# category TLCore
# catalog-ctan /dviware/dvidvi
# catalog-date 2012-05-07 18:30:58 +0200
# catalog-license other-free
# catalog-version 1.0
Name:		texlive-dvidvi
Version:	1.0
Release:	3
Summary:	Convert one DVI file into another
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/dviware/dvidvi
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dvidvi.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires:	texlive-dvidvi.bin

%description
The output DVI file's contents are specified by page selection
commands; series of pages and page number ranges may be
specified, as well as inclusions and exclusions.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_mandir}/man1/dvidvi.1*
%{_texmfdir}/doc/man/man1/dvidvi.man1.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1


%changelog
* Tue Aug 07 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-3
+ Revision: 812235
- Update to latest release.

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-2
+ Revision: 751194
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 718278
- texlive-dvidvi
- texlive-dvidvi
- texlive-dvidvi
- texlive-dvidvi

