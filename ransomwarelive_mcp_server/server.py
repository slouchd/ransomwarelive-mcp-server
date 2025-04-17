#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import httpx
import logging
from mcp.server.fastmcp import FastMCP

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

# Create an MCP server
mcp = FastMCP("Ransomware Live MCP Server")


def create_api_request(endpoint: str) -> dict:
    """
    Send a GET request to one of the ransomware.live API endpoints to retrieve data

    :param endpoint: API endpoint to retrieve data from using a GET request
    :return: dict object of response data
    """
    api_url = f"https://api.ransomware.live/v2/{endpoint}"
    request_headers = {
        "Accept": "application/json"
    }

    try:
        log.info(f"Attempting to send GET request to {api_url}")
        response = httpx.get(url=api_url, headers=request_headers)
        response.raise_for_status()
        return response.json()
    except httpx.RequestError as req_exc:
        log.error(f"Exception raised during HTTP GET request to {api_url} - {req_exc}")
        return {"error": f"Exception raised during HTTP GET request to {api_url} - {req_exc}"}


@mcp.tool()
def get_recent_victims(shorter_context: bool = True) -> dict:
    """
    Get details about the last 100 victims claimed by ransomware groups that are tracked by ransomware.live

    :param shorter_context: bool to determine whether to return a shorter response context or not
    :return: dict object with recent victims
    """
    if shorter_context:
        shorter_context_res = {"recent_victims": []}
        endpoint_response = create_api_request(endpoint="recentvictims")

        for victim in endpoint_response:
            shorter_context_res["recent_victims"].append(victim["victim"])

        return shorter_context_res
    else:
        return create_api_request(endpoint="recentvictims")


@mcp.tool()
def get_sector_counts() -> dict:
    """
    Get the number of victims by sector that are tracked by ransomware.live

    :return: dict object with victim counts by sector
    """
    return create_api_request(endpoint="sectors")


@mcp.tool()
def get_victims_by_sector(sector: str, shorter_context: bool = True) -> dict:
    """
    Get details about victims within a specific sector

    :param sector: sector to find victims within
    :param shorter_context: bool to determine whether to return a shorter response context or not
    :return: dict object with victims by specific sector
    """
    if shorter_context:
        shorter_context_res = {"victims_by_sector": []}
        endpoint_response = create_api_request(endpoint=f"sectorvictims/{sector}")

        for victim in endpoint_response:
            victim_and_group = {"victim": victim["victim"], "group": victim["group"]}
            shorter_context_res["victims_by_sector"].append(victim_and_group)

        return shorter_context_res
    else:
        return create_api_request(endpoint=f"sectorvictims/{sector}")


@mcp.tool()
def get_victims_by_sector_countrycode(sector: str, countrycode: str, shorter_context: bool = True) -> dict:
    """
    Get details about victims within a specific sector and country code

    :param sector: sector to find victims within
    :param countrycode: country to find victims within
    :param shorter_context: bool to determine whether to return a shorter response context or not
    :return: dict object with victims by specific sector and country code
    """
    if shorter_context:
        shorter_context_res = {"victims_by_sector_countrycode": []}
        endpoint_response = create_api_request(endpoint=f"sectorvictims/{sector}/{countrycode}")

        for victim in endpoint_response:
            victim_and_group = {"victim": victim["victim"], "group": victim["group"]}
            shorter_context_res["victims_by_sector_countrycode"].append(victim_and_group)

        return shorter_context_res
    else:
        return create_api_request(endpoint=f"sectorvictims/{sector}/{countrycode}")


@mcp.tool()
def get_victims_by_countrycode(countrycode: str) -> dict:
    """
    Get details about victims within a specific country

    :param countrycode: country to find victims within
    :return: dict object with victims by 2-letter country code
    """
    return create_api_request(endpoint=f"countryvictims/{countrycode}")


@mcp.tool()
def get_victims_by_year(year: int, shorter_context: bool = True) -> dict:
    """
    Get details about the victims within a specific year

    :param year: a year expressed as an integer
    :param shorter_context: bool to determine whether to return a shorter response context or not
    :return: dict object with victims by year
    """
    if shorter_context:
        shorter_context_res = {"victims_by_year": []}
        endpoint_response = create_api_request(endpoint=f"victims/{year}")

        for victim in endpoint_response:
            victim_and_group = {"victim": victim["victim"], "group": victim["group"]}
            shorter_context_res["victims_by_year"].append(victim_and_group)

        return shorter_context_res
    else:
        return create_api_request(endpoint=f"victims/{year}")


@mcp.tool()
def get_victims_by_year_month(year: int, month: int, shorter_context: bool = True) -> dict:
    """
    Get details about the victims within a specific year and month

    :param year: a year expressed as an integer
    :param month: a month expressed as an integer
    :param shorter_context: bool to determine whether to return a shorter response context or not
    :return: dict object with victims by year and month
    """
    if shorter_context:
        shorter_context_res = {"victims_by_year_month": []}
        endpoint_response = create_api_request(endpoint=f"victims/{year}/{month}")

        for victim in endpoint_response:
            victim_and_group = {"victim": victim["victim"], "group": victim["group"]}
            shorter_context_res["victims_by_year_month"].append(victim_and_group)

        return shorter_context_res
    else:
        return create_api_request(endpoint=f"victims/{year}/{month}")


@mcp.tool()
def get_victims_by_keyword(keyword: str) -> dict:
    """
    Query for victims by keyword

    :param keyword: keyword string used to query for ransomware victims
    :return: dict object with victims queried by keyword
    """
    return create_api_request(endpoint=f"searchvictims/{keyword}")


@mcp.tool()
def get_all_ransomware_groups(shorter_context: bool = True) -> dict:
    """
    Get details about all ransomware groups that are tracked by ransomware.live

    :param shorter_context: bool to determine whether to return a shorter response context or not
    :return: dict object with ransomware groups details
    """
    if shorter_context:
        shorter_context_res = {"ransomware_groups": []}
        endpoint_response = create_api_request(endpoint="groups")

        for group in endpoint_response:
            shorter_context_res["ransomware_groups"].append(group["name"])

        return shorter_context_res
    else:
        return create_api_request(endpoint="groups")


@mcp.tool()
def get_ransomware_group(group_name: str) -> dict:
    """
    Get details about a specific ransomware group according to ransomware.live

    :param group_name: name of the ransomware group
    :return: dict object with ransomware group details
    """
    return create_api_request(endpoint=f"group/{group_name}")


@mcp.tool()
def get_ransomware_group_victims(group_name: str, shorter_context: bool = True) -> dict:
    """
    Get all victims of a specific ransomware group according to ransomware.live

    :param group_name: name of the ransomware group
    :param shorter_context: bool to determine whether to return a shorter response context or not
    :return: dict object with victims from a ransomware group
    """
    if shorter_context:
        shorter_context_res = {"ransomware_group_victims": []}
        endpoint_response = create_api_request(endpoint=f"groupvictims/{group_name}")

        for victim in endpoint_response:
            shorter_context_res["ransomware_group_victims"].append(victim["victim"])

        return shorter_context_res
    else:
        return create_api_request(endpoint=f"groupvictims/{group_name}")


def main():
    """Initialize and run the server"""
    log.info("Starting the ransomware.live MCP server")
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
