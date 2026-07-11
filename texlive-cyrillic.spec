%global tl_name cyrillic
%global tl_revision 71408

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Support for Cyrillic fonts in LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/required/cyrillic
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cyrillic.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cyrillic.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cyrillic.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(cyrillic-bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This bundle of macros files provides macro support (including font
encoding macros) for the use of Cyrillic characters in fonts encoded
under the T2* and X2 encodings. These encodings cover (between them)
pretty much every language that is written in a Cyrillic alphabet. This
directory is part of the LaTeX "required" distribution.

