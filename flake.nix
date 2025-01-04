{
  description = "A Nix-flake-based Python development environment";

  inputs.nixpkgs.url = "pinned-nixpkgs";
  
  outputs = { self, nixpkgs }:
    let
      supportedSystems = [ "x86_64-linux" "aarch64-linux" "x86_64-darwin" "aarch64-darwin" ];
      forEachSupportedSystem = f: nixpkgs.lib.genAttrs supportedSystems (system: f {
        pkgs = import nixpkgs { inherit system; };
      });
    in
    {
      devShells = forEachSupportedSystem ({ pkgs }: {
        default = let
          python = pkgs.python311.override {
            self = python;
            packageOverrides = pyfinal: pyprev: {
              
            };
          };
        in
        pkgs.mkShell {
          venvDir = ".venv";
          packages = with pkgs; [ 
            (python.withPackages (python-pkgs: with python-pkgs; [
              pip
              venvShellHook
            ]))
          ];

          postVenvCreation = ''
            unset SOURCE_DATE_EPOCH
          '';
        };
      });
    };
}
