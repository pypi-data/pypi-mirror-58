from .abstractentity import AbstractEntity
from .utils.http_request import http
from .utils.wrap_tools import make_repr

class Song(AbstractEntity):
    """Class that represents Geometry Dash/Newgrounds songs.
    This class is derived from :class:`.AbstractEntity`.
    """
    def __init__(self, **options):
        super().__init__(**options)
        self.options = options

    def __repr__(self):
        info = {
            'id': self.id,
            'name': repr(self.name),
            'author': repr(self.author)
        }
        return make_repr(self, info)

    @property
    def id(self):
        """:class:`int`: An ID of the song."""
        return self.options.get('id', 0)

    @property
    def name(self):
        """:class:`str`: A name of the song."""
        return self.options.get('name', '')

    @property
    def size(self):
        """:class:`float`: A float representing size of the song, in megabytes."""
        return self.options.get('size', 0.0)

    @property
    def author(self):
        """:class:`str`: An author of the song."""
        return self.options.get('author', '')

    @property
    def link(self):
        """:class:`str`: A link to the song on Newgrounds, e.g. ``.../audio/listen/id``."""
        return self.options.get('links', {}).get('normal', '')

    @property
    def dl_link(self):
        """:class:`str`: A link to download the song, used in :meth:`.Song.download`."""
        return self.options.get('links', {}).get('download', '')

    def is_custom(self):
        """:class:`bool`: Indicates whether the song is custom or not."""
        return self.options.get('custom', False)

    async def download(self):
        """|coro|

        Download a song from Newgrounds.

        Returns
        -------
        :class:`bytes`
            A song as bytes.
        """
        resp = await http.normal_request(self.dl_link)
        return await resp.content.read()
