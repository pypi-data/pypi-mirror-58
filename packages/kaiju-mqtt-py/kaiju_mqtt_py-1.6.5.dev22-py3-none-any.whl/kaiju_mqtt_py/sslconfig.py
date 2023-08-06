# Copyright Netflix, 2019
import json
from pathlib import Path
from typing import Text


class SslConfig:
    def __init__(self, name: Text) -> None:
        self.dir = Path(name)
        self.rootcert = self.dir / "rootca.crt"
        self.publickey = self.dir / "public.key"
        self.privatekey = self.dir / "private.key"
        self.certificate = self.dir / "cert.pem"
        self.overridefile = self.dir / "host.json"
        self.host = str(self.dir.parts[-1])
        self.port = 8883 if self.iscomplete() else 1883

        if self.overridefile.exists():
            with open(self.overridefile) as f:
                try:
                    overrides = json.load(f)
                    if "host" in overrides:
                        self.host = overrides["host"]
                    if "port" in overrides:
                        self.port = overrides["port"]
                except json.JSONDecodeError:
                    print(f"Found invalid JSON in this file, ignoring it: {str(self.overridefile)}")

    def __repr__(self) -> Text:
        return self.dir.__repr__()

    def __str__(self) -> Text:
        return "mqtt://" + self.host + ":" + str(self.port)

    def __bool__(self) -> bool:
        return self.dir.exists()

    def exists(self) -> bool:
        return self.dir.exists()

    def iscomplete(self) -> bool:
        files = [self.rootcert, self.publickey, self.privatekey, self.certificate]
        parts = [x.exists() for x in files]
        return all(parts)
