#!/usr/bin/python3
"""
    init file for the models package
"""
from .engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
