%global tl_name dvidvi
%global tl_revision 75712

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Convert one DVI file into another
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/dviware/dvidvi
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dvidvi.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dvidvi.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(dvidvi.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The output DVI file's contents are specified by page selection commands;
series of pages and page number ranges may be specified, as well as
inclusions and exclusions. It is now maintained as part of TeX Live.

