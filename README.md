# ShareX Flask Server

Custom Flask webserver designed for sharex 


Upload files using SFTP or whatever you use into /files from the **project** root


set necessary configuration in `start.sh` - rename `start_example.sh` to `start.sh` and input desired config


to deploy w/ default config: 

```
apt install gunicorn
```

```
<python_cmd> -m pip install -r requirements.txt
```

configure reverse proxy to point to the port in `start.sh`
