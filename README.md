# code-events-infrastructure

Infrastructure layer for <https://github.com/pythoneda-shared-artifact/code-events>.

## How to declare it in your flake

Check the latest tag of the artifact repository: https://github.com/pythoneda-shared-artifact/code-events-infrastructure-artifact/tags, and use it instead of the `[version]` placeholder below.

```nix
{
  description = "[..]";
  inputs = rec {
    [..]
    pythoneda-shared-artifact-code-events-infrastructure = {
      [optional follows]
      url =
        "github:pythoneda-shared-artifact/code-events-infrastructure-artifact/[version]?dir=code-events-infrastructure";
    };
  };
  outputs = [..]
};
```

Should you use another PythonEDA modules, you might want to pin those also used by this project. The same applies to [https://nixos/nixpkgs](nixpkgs "nixpkgs") and [https://github.com/numtide/flake-utils](flake-utils "flake-utils").

The Nix flake is under the [https://github.com/pythoneda-shared-artifact/code-events-infrastructure-artifact/tree/main/code-events-infrastructure](code-events-infrastructure "code-events-infrastructure") folder of <https://github.com/pythoneda-shared-artifact/code-events-infrastructure-artifact>.



