%global tl_name luaprogtable
%global tl_revision 56113

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Programmable table interface for LuaLaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/luatex/latex/luaprogtable
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/luaprogtable.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/luaprogtable.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package allows you to modify a cell based on the contents of other
cells using LaTeX macros.

