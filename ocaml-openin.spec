Name:           ocaml-openin
Version:        20070524
Release:        %mkrel 1
Summary:        OCaml syntax to locally open modules
License:        Public Domain
Group:          Development/Other
URL:            http://alain.frisch.fr/soft#openin
Source0:        http://alain.frisch.fr/info/openin-%{version}.tar.gz
Source1:        openin-META
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml-findlib
BuildRequires:  camlp4

%description
This package implements a Camlp4 syntax extension for Objective
Caml. It adds the syntactic construction:

open M in e

that can appear in any context where an expression is expected. M is
an arbitrary module expression (not only qualified names as for usual
open statements) and e is an expression.

%prep
%setup -q -n openin-%{version}
cp %{SOURCE1} META

%build
make
sed -i -e "s/@VERSION@/%{version}/" META

%install
rm -rf %{buildroot}
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR $OCAMLFIND_DESTDIR/stublibs
ocamlfind install openin META pa_openin.cmo

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%dir %{_libdir}/ocaml/openin
%{_libdir}/ocaml/openin/META
%{_libdir}/ocaml/openin/pa_openin.cmo

