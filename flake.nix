{
    description = "TODO";
    inputs = {
        nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";
    };
    outputs = { self, nixpkgs }: {
        devShells = nixpkgs.mkShellNoCC {
            name     = "TODO";
            version  = "0.0.0";
            packages = [
                python3
            ];
        };
    };
}
