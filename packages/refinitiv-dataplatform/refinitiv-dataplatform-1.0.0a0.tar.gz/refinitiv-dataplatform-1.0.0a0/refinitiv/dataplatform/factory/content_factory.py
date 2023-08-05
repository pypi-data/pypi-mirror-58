# coding: utf8

from pandas import DataFrame
from refinitiv.dataplatform.content.news.news_headlines import NewsHeadlines
from refinitiv.dataplatform.content.news.news_story import NewsStory
from refinitiv.dataplatform.function.tools import to_utc_date, to_datetime
from refinitiv.dataplatform.content.streaming.streamingprice import StreamingPrice
from refinitiv.dataplatform.core.session import ElektronError


__all__ = ["ContentFactory",
            "get_last_result",
           "get_last_status", "get_last_error_status",
           "get_reference_data",
           "get_snapshot",
           "open_realtime_cache", "close_realtime_cache",
           "get_historical_price_events", "get_historical_price_summaries",
           "get_news_headlines", "get_news_story", "get_news_story_async",
           "get_next_headlines", "get_prev_headlines",
           "search", "lookup"]


class ContentFactory:

    __content_factory = None
    __last_error_status = None
    __last_result = None

    def __init__(self):
        pass

    @classmethod
    def get_default_session(cls):
        from refinitiv.dataplatform.function import get_default_session
        return get_default_session()

    @classmethod
    def _get_content_factory(cls):
        return ContentFactory()
        # following code limit ContentFactory instance to 1 singleton
        # if cls.__content_factory is None:
        #     cls.__content_factory = ContentFactory()
        # return cls.__content_factory

    @classmethod
    def _get_last_result(cls):
        return cls.__last_result

    @classmethod
    def _get_last_status(cls):
        if cls.__last_result:
            return cls.__last_result.status

    @classmethod
    def _get_last_error_status(cls):
        return cls.__last_error_status

    @staticmethod
    def create_market_price_with_params(mp_params):
        if isinstance(mp_params, StreamingPrice.Params):
            mp = StreamingPrice(session=mp_params._session,
                                name=mp_params._name,
                                service=mp_params._service,
                                fields=mp_params._fields,
                                streaming=mp_params._streaming,
                                extended_params=mp_params._extended_params,
                                on_refresh=mp_params._on_refresh_cb,
                                on_update=mp_params._on_update_cb,
                                on_status=mp_params._on_status_cb,
                                on_complete=mp_params._on_complete_cb)
            return mp
        else:
            raise Exception("Wrong MarketPrice.Param parameter")

    @staticmethod
    def create_market_price(session,
                            name,
                            service=None,
                            fields=None,
                            streaming=True,
                            extended_params=None,
                            on_refresh=None,
                            on_update=None,
                            on_status=None,
                            on_complete=None):
        return StreamingPrice(session=session,
                              name=name,
                              service=service,
                              fields=fields,
                              streaming=streaming,
                              extended_params=extended_params,
                              on_refresh=on_refresh,
                              on_update=on_update,
                              on_status=on_status,
                              on_complete=on_complete)

    @classmethod
    def _get_reference_data(cls,
                            universe,
                            fields=[],
                            parameters={}):
        from refinitiv.dataplatform.pricing.pricing_ import Pricing
        session = cls.get_default_session()
        pricing = Pricing(session)
        reference_data = pricing.get_snapshot(universe, fields, parameters)
        cls.__last_result = reference_data
        if reference_data.is_success and reference_data.data and reference_data.data.df is not None:
            return reference_data.data.df
        else:
            cls.__last_error_status = reference_data.status
            return None

    @classmethod
    def _get_snapshot(cls, universe, fields, options={}):
        from refinitiv.dataplatform.pricing.pricing_ import Pricing

        session = ContentFactory.get_default_session()
        pricing = Pricing(session)
        price_data = pricing.get_snapshot(universe, fields)

        cls.__last_result = price_data
        if price_data.is_success and price_data.data and price_data.data.df is not None:
            return price_data.data.df
        else:
            cls.__last_error_status = price_data.status
            return None

    @classmethod
    def _open_realtime_cache(cls,
                             universe,
                             fields=[]):
        from refinitiv.dataplatform.pricing.pricing_ import PriceCache

        session = ContentFactory.get_default_session()
        price_cache = PriceCache(session, universe, fields)
        price_cache.open()
        return price_cache

    @classmethod
    def _close_realtime_cache(cls, price_cache):
        price_cache.close()

    @classmethod
    def _get_historical_price_events(cls,
                                     universe,
                                     eventTypes=None,
                                     start=None,
                                     end=None,
                                     adjustments=[],
                                     count=1,
                                     fields=[],
                                     on_response=None,
                                     closure=None):
        from refinitiv.dataplatform.content.data.historical_pricing import HistoricalPricing

        session = ContentFactory.get_default_session()
        historical_pricing = HistoricalPricing(session=session, on_response=on_response)
        historic_events = historical_pricing.get_events(universe=universe,
                                                        eventTypes=eventTypes,
                                                        start=start,
                                                        end=end,
                                                        adjustments=adjustments,
                                                        count=count,
                                                        fields=fields,
                                                        closure=closure)
        cls.__last_result = historic_events
        if historic_events.is_success and historic_events.data and historic_events.data.df is not None:
            return historic_events.data.df
        else:
            cls.__last_error_status = historic_events.status
            return None

    @classmethod
    def _get_historical_price_summaries(cls,
                                        universe,
                                        interval=None,
                                        start=None,
                                        end=None,
                                        adjustments=None,
                                        sessions=[],
                                        count=1,
                                        fields=[],
                                        on_response=None,
                                        closure=None):
        from refinitiv.dataplatform.content.data.historical_pricing import HistoricalPricing
        session = ContentFactory.get_default_session()
        historical_pricing = HistoricalPricing(session=session, on_response=on_response)
        historic_summaries = historical_pricing.get_summaries(universe=universe,
                                                              interval=interval,
                                                              start=start,
                                                              end=end,
                                                              adjustments=adjustments,
                                                              sessions=sessions,
                                                              count=count,
                                                              fields=fields,
                                                              closure=closure)
        cls.__last_result = historic_summaries
        if historic_summaries.is_success and historic_summaries.data and historic_summaries.data.df is not None:
            return historic_summaries.data.df
        else:
            cls.__last_error_status = historic_summaries.status
            return None

    _news_headline_endpoint = None
    @classmethod
    def _get_news_headline_endpoint(cls):
        _news_headline_endpoint = NewsHeadlines(cls.get_default_session())
        return _news_headline_endpoint

    @classmethod
    def _get_news_headlines(cls,
                            query="Topic:TOPALL and Language:LEN",
                            count=10,
                            date_from=None,
                            date_to=None):
        headline_endpoint = cls._get_news_headline_endpoint()
        headlines = headline_endpoint.get_headlines(query=query,
                                                    count=count,
                                                    date_from=date_from,
                                                    date_to=date_to)
        cls.__last_result = headlines
        if headlines is not None:
            if headlines.is_success:
                return headlines.data.df
            else:
                cls.__last_error_status = headline_endpoint.status
                return None
        else:
            cls.__last_error_status = headline_endpoint.status
            return None

    @classmethod
    def _get_next_headlines(cls, headlines_response):
        return cls._get_link_headlines(headlines_response=headlines_response,
                                       link_type="next")

    @classmethod
    def _get_prev_headlines(cls, headlines_response):
        return cls._get_link_headlines(headlines_response=headlines_response,
                                       link_type="prev")

    @classmethod
    def _get_link_headlines(cls, headlines_response, link_type=None):
        headline_endpoint = cls._get_news_headline_endpoint()
        if isinstance(headlines_response, NewsHeadlines.NewsHeadlinesResponse):
            if headlines_response.data and headlines_response.data.raw:
                links_headlines = headlines_response.data.raw.get("meta")
                if links_headlines:
                    _link = links_headlines.get(link_type)
                    if link_type == "next":
                        _other_headlines_result = headline_endpoint.get_next_headlines(link_next=_link)
                    else:
                        _other_headlines_result = headline_endpoint.get_prev_headlines(link_prev=_link)
                    cls.__last_result = _other_headlines_result
                    if _other_headlines_result.is_success and _other_headlines_result.data and _other_headlines_result.data.df is not None:
                        cls.__last_result = _other_headlines_result
                        return _other_headlines_result.data.df
                    else:
                        cls.__last_error_status = _other_headlines_result.status
                        return None
            raise ElektronError(-1,
                                f"Can't get {link_type} headlines from empty object {headlines_response}({type(headlines_response)})")
        elif isinstance(headlines_response, DataFrame):
            if hasattr(headlines_response, f"_link_{link_type}"):
                if link_type == "next":
                    _link = headlines_response._link_next
                    _other_headlines_result = headline_endpoint.get_next_headlines(link_next=_link)
                else:
                    if hasattr(headlines_response, "_link_prev"):
                        _link = headlines_response._link_prev
                        _other_headlines_result = headline_endpoint.get_prev_headlines(link_prev=_link)
                    else:
                        raise ElektronError(-1,
                            f"Can't get {link_type} headlines from object {headlines_response}({type(headlines_response)})")
                cls.__last_result = _other_headlines_result
                if _other_headlines_result.is_success and _other_headlines_result.data and _other_headlines_result.data.df is not None:
                    return _other_headlines_result.data.df
                else:
                    cls.__last_error_status = _other_headlines_result.status
                    return None
        raise ElektronError(-1,
            f"Can't get {link_type} headlines from object {headlines_response}({type(headlines_response)})")

    _news_story_endpoint = None

    @classmethod
    def _get_news_story_endpoint(cls):
        return NewsStory(cls.get_default_session())
        if cls._news_story_endpoint is None:
            session = ContentFactory.get_default_session()
            cls._news_story_endpoint = NewsStory(session)
        return cls._news_story_endpoint

    @classmethod
    def _get_news_story(cls, story_id):
        story = cls._get_news_story_endpoint().get_story(story_id=story_id)
        cls.__last_result = story
        if story.is_success and story.data and story.data.text is not None:
            cls.__last_result = story
            return story.data.text
        else:
            cls.__last_error_status = story.status
            return None

    @classmethod
    async def _get_news_story_async(cls, story_id):
        story = await cls._get_news_story_endpoint().get_story_async(story_id=story_id)
        cls.__last_result = story
        if story.is_success and story.data and story.data.text is not None:
            cls.__last_result = story
            return story.data.text
        else:
            cls.__last_error_status = story.status
            return None

    @classmethod
    def _search(cls):
        cls.__last_result = "Not implemented"
        return None

    @classmethod
    def _lookup(cls):
        cls.__last_result = "Not implemented"
        return None


def get_last_result():
    return ContentFactory._get_content_factory()._get_last_result()


def get_last_status():
    return ContentFactory._get_content_factory()._get_last_status()


def get_last_error_status():
    return ContentFactory._get_content_factory()._get_last_error_status()


def get_reference_data(universe,
                       fields=[],
                       parameters={}):
    return ContentFactory._get_content_factory()._get_reference_data(universe=universe,
                                                                     fields=fields,
                                                                     parameters=parameters)


def get_realtime_snapshot(universe, fields, options={}):
    return ContentFactory._get_content_factory()._get_snapshot(universe=universe,
                                                               fields=fields,
                                                               options=options)
get_snapshot = get_realtime_snapshot


def open_realtime_cache(universe,
                        fields=[]):
    return ContentFactory._get_content_factory()._open_realtime_cache(universe=universe,
                                                                      fields=fields)


def close_realtime_cache(price_cache):
    return ContentFactory._get_content_factory()._close_realtime_cache(price_cache=price_cache)


def get_historical_price_events(universe,
                                eventTypes=None,
                                start=None,
                                end=None,
                                adjustments=[],
                                count=1,
                                fields=[],
                                on_response=None,
                                closure=None):
    return ContentFactory._get_content_factory()._get_historical_price_events(universe=universe,
                                                                              eventTypes=eventTypes,
                                                                              start=start,
                                                                              end=end,
                                                                              adjustments=adjustments,
                                                                              count=count,
                                                                              fields=fields,
                                                                              on_response=on_response,
                                                                              closure=closure)


def get_historical_price_summaries(universe,
                                   interval=None,
                                   start=None,
                                   end=None,
                                   adjustments=None,
                                   sessions=[],
                                   count=1,
                                   fields=[],
                                   on_response=None,
                                   closure=None):
    return ContentFactory._get_historical_price_summaries(universe=universe,
                                                          interval=interval,
                                                          start=start,
                                                          end=end,
                                                          adjustments=adjustments,
                                                          sessions=sessions,
                                                          count=count,
                                                          fields=fields,
                                                          on_response=on_response,
                                                          closure=closure)


def get_news_headlines(query="Topic:TOPALL and Language:LEN",
                       count=10,
                       date_from=None,
                       date_to=None):
    return ContentFactory._get_news_headlines(query=query,
                                              count=count,
                                              date_from=date_from,
                                              date_to=date_to)


def get_next_headlines(headlines_response):
    return ContentFactory._get_next_headlines(headlines_response)


def get_prev_headlines(headlines_response):
    return ContentFactory._get_prev_headlines(headlines_response)


def get_news_story(story_id):
    return ContentFactory._get_news_story(story_id)


async def get_news_story_async(story_id):
    result = await ContentFactory._get_news_story_async(story_id)
    return result


def search():
    return ContentFactory._get_content_factory()._search()

def get_search_metadata():
    return ContentFactory._get_content_factory()._search_metadata()

def lookup():
    return ContentFactory._get_content_factory()._lookup()
