# PyMixConf

because i miss mix's config loader when i can't use elixir

loads environment-specific config from file

so what this essentially does is load config from 3 files, of the pattern

- `config.???`
- `ENV.config.???`
- `ENV.secret.???`

where `???` is an extension. `config.???` is base config, `ENV.config.???` is
any standard config for an environment, and `ENV.secret.???` is deployment
secrets that you don't want to commit to your VCS.

## Usage

first you'll need to create the files required. let's assume you want to
use yaml.

```bash
mkdir -p config
touch config/config.yaml config/{dev,test,prod}.{config,secret}.yaml
echo "*.secret.yaml" >> .gitignore
```

now you can shove stuff in those files. idk. go wild.

then to load it:

```python
from pymixconf import YamlConfig

loader = YamlConfig()
my_config = loader.load_config()
```

and it'll load from your development config

it'll load from `CONFIG_ENV` by default.

your options are as follows:

```python
YamlConfig(
  config_directory="my_conf", # the directory we want to load from
  environment_key="CONFIG_ENV" # the env value to load files based on
)
```

you can also use `pymixconf.JSONConf` if you want, or if you're a real
loose cannon you can subclass `pymixconf.mixconf.MixConf` and implement
`load_from_file(self, filename: str) -> dict` yourself.

whatever you want i guess
