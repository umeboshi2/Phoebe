from pyramid.config import Configurator
from sqlalchemy import engine_from_config
from pyramid_beaker import session_factory_from_settings

from trumpet.security import authn_policy, authz_policy

from trumpet.models.base import DBSession, Base
from trumpet.models.usergroup import populate
from trumpet.models.wiki import populate_wiki
from trumpet.models.rssdata import populate_feeds
from trumpet.models.base import initialize_sql

from trumpet.config.base import basetemplate, configure_base_layout
from trumpet.config.static import configure_static
from trumpet.config.wiki import configure_wiki
from trumpet.config.rssviewer import configure_rssviewer
from trumpet.config.login import configure_login


from phoebe.models import (
    MyModel,
    )

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    settings['db.sessionmaker'] = DBSession
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    if True:
        import transaction
        Base.metadata.create_all(engine)
        with transaction.manager:
            model = MyModel(name='one', value=1)
            DBSession.add(model)
            initialize_sql(engine, [populate,
                                    populate_wiki,
                                    populate_feeds])
    session_factory = session_factory_from_settings(settings)
    root_factory = 'trumpet.resources.RootGroupFactory'
    request_factory = 'trumpet.request.AlchemyRequest'
    config = Configurator(settings=settings,
                          root_factory=root_factory,
                          request_factory=request_factory,
                          authentication_policy=authn_policy,
                          authorization_policy=authz_policy,
                          session_factory=session_factory)
    configure_static(config)
                          
    #config.include('pyramid_fanstatic')
    configure_base_layout(config)

    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_view('phoebe.views.MainViewer', route_name='home',
                    renderer=basetemplate,
                    layout='base')
    
    configure_login(config)

    #configure_rssviewer(config, '/rssviewer')
    config.add_route('rssviewer', '/rssviewer/{context}/{feed}')
    config.add_view('trumpet.views.rssviewer.MainViewer',
                    route_name='rssviewer', layout='base')

    configure_wiki(config, '/wiki')

    return config.make_wsgi_app()

