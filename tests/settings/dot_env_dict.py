from dj_configurator import Configuration, values


class DotEnvConfiguration(Configuration):
    DOTENV = {
        "path": "tests/simple_project/.env",
        "override": True,
    }

    DOTENV_VALUE = values.Value()
    DOTENV_OVERRIDE = values.Value("Not overridden")
