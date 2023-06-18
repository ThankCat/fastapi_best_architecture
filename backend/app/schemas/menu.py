#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from datetime import datetime

from pydantic import Field

from backend.app.common.enums import MenuType, StatusType
from backend.app.schemas.base import SchemaBase


class MenuBase(SchemaBase):
    name: str
    parent_id: int = Field(default=None, ge=1, description='菜单父级ID')
    sort: int = Field(default=0, ge=0, description='排序')
    icon: str | None = None
    path: str | None = None
    menu_type: MenuType = Field(default=MenuType.directory, ge=0, description='菜单类型（0目录 1菜单 2按钮）')
    component: str | None = None
    perms: str | None = None
    status: StatusType = Field(default=StatusType.enable)
    remark: str | None = None


class CreateMenu(MenuBase):
    pass


class UpdateMenu(MenuBase):
    pass


class GetAllMenu(MenuBase):
    id: int
    create_user: int
    update_user: int = None
    created_time: datetime
    updated_time: datetime | None = None

    class Config:
        orm_mode = True
