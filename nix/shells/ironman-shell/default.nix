{ pkgs, stdenv, ... }:
  let
    myPythonPackages = py:
      with py; [
        black
        debugpy
        flake8
        qtile
      ];
    myPython = pkgs.python3.withPackages myPythonPackages;
  in
stdenv.mkDerivation {
  name = "ironman-shell";
  nativeBuildInputs = with pkgs; [
    myPython
    nix-index
    nix-tree
  ];

  shellHook = ''
    export VIRTUAL_ENV="${myPython}"
  '';
}
