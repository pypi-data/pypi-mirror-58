from __future__ import annotations

from dataclasses import dataclass
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Optional, Union, TYPE_CHECKING, Type, Dict, Any

import frontmatter  # type: ignore
from jinja2 import Template
from mistune import Markdown  # type: ignore

from .content import Content
from .lwmd import LwRenderer, TableOfContents

if TYPE_CHECKING:
    from lightweight import GenPath, GenContext


@dataclass(frozen=True)
class MarkdownPage(Content):
    template: Template  # Jinja2 template
    source: str  # the contents of a markdown file
    path: Path  # path to the markdown file

    renderer: Type[LwRenderer]

    title: Optional[str]
    summary: Optional[str]
    created: Optional[datetime]
    updated: Optional[datetime]
    order: Optional[Union[int, float]]

    options: Dict[str, Any]

    def render(self, ctx: GenContext):
        link_mapping = self.map_links(ctx)
        renderer = self.renderer(link_mapping)
        html = Markdown(renderer).render(self.source)
        toc = renderer.table_of_contents(level=3)
        preview_html = self.extract_preview(html)
        return RenderedMarkdown(
            html=html,
            preview_html=preview_html,
            toc=toc,
            title=self.title,
            summary=self.summary,
            created=self.created,
            updated=self.updated,
            options=self.options,
        )

    @staticmethod
    def map_links(ctx: GenContext):
        link_mapping = {str(task.path): task.path.url for task in ctx.tasks}
        link_mapping.update({
            str(task.content.path): task.path.url
            for task in ctx.tasks
            if isinstance(task.content, MarkdownPage)
        })
        return link_mapping

    @staticmethod
    def extract_preview(html):
        preview_split = html.split('<!--preview-->', maxsplit=1)
        preview_html = preview_split[0] if len(preview_split) == 2 else None
        return preview_html

    def write(self, path: GenPath, ctx: GenContext):
        path.create(self.template.render(
            site=ctx.site,
            ctx=ctx,
            source=self,
            markdown=self.render(ctx)
        ))


def markdown(md_path: Union[str, Path], template: Template, *, renderer=LwRenderer) -> MarkdownPage:
    path = Path(md_path)
    with path.open() as f:
        source = f.read()
    post = frontmatter.loads(source)
    title = post.get('title', None)
    summary = post.get('summary', None)
    created = post.get('created', None)
    updated = post.get('updated', created)
    if created is not None:
        assert isinstance(created, datetime), '"created" is not a valid datetime object'
        created = created.replace(tzinfo=timezone.utc)
    if updated is not None:
        assert isinstance(updated, datetime), '"updated" is not a valid datetime object'
        updated = updated.replace(tzinfo=timezone.utc)
    order = post.get('order', None)
    return MarkdownPage(
        template=template,
        source=post.content,
        path=path,

        renderer=renderer,

        title=title,
        summary=summary,
        created=created,
        updated=updated,
        order=order,
        options=dict(post),
    )


@dataclass(frozen=True)
class RenderedMarkdown:
    html: str
    preview_html: str
    toc: TableOfContents

    title: Optional[str]
    summary: Optional[str]
    updated: Optional[date]
    created: Optional[date]
    options: Dict[str, Any]
