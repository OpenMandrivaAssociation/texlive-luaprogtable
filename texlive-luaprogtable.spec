Name:		texlive-luaprogtable
Version:	56113
Release:	2
Summary:	Programmable table interface for LuaLaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/luaprogtable
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luaprogtable.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luaprogtable.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package allows you to modify a cell based on the contents
of other cells using LaTeX macros.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/lualatex/luaprogtable
%doc %{_texmfdistdir}/doc/lualatex/luaprogtable

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
