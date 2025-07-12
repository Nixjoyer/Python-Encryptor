{
  description = "Python encryption script with MD5 and Fernet";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-25.05";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
        myPython = pkgs.python3.withPackages (ps: [ ps.cryptography ]);
      in {
        # Dev shell (nix develop)
        devShell = pkgs.mkShell {
          buildInputs = [ myPython ];
        };

        # nix run
        packages.default = pkgs.writeShellApplication {
          name = "encryptor";
          runtimeInputs = [ myPython ];
          text = ''
            ${myPython}/bin/python3 ${./encryptor.py}
          '';
        };
      }
    );
}

