{
  description = "My Nix Flakes";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-23.05";
    snowfall-lib = {
      inputs.nixpkgs.follows = "nixpkgs";
      url = "github:snowfallorg/lib";
    };
    unstable.url = "github:nixos/nixpkgs/nixos-unstable";
  };

  outputs = inputs: let
    lib = inputs.snowfall-lib.mkLib {
      inherit inputs;
      src = ./nix;

      snowfall = {
        meta = {
          name = "ironman";
          title = "Ironman Home Config";
        };
        namespace = "ironman";
      };
    };
  in lib.mkFlake {
    channels-config = {
      allowUnfree = true;
    };

    alias = {
      shells.default = "ironman-shell";
    };
  };
}
