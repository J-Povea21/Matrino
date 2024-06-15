# Matrino
Welcome to Matrino's API!

## Installation
Create and `.env` file in the root of the project and add the following variable
```env
PORT=3000 # Or whatever port you want the container to run
```

> Note: In case you decide to call your `.env` file in different way, make sure to
> run `docker compose --enf-file ./.your_env_file.env build` in order to load the
> correct environment file. You need to do the same for the `docker compose up`
> command

Then you just need to run
```shell
docker compose build && docker compose up --watch
```

And that's all :). With this you'll be able to run the Matrino API
