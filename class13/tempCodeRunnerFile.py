html_doc= """
<li data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    <a tabindex="-1" id="item-33f5cbab-5964-4909-b856-d81359a97d6e" href="https://github.com/zainalvi110" role="menuitem" data-view-component="true" class="ActionListContent">
        <span data-view-component="true" class="ActionListItem-label">
            Your GitHub.com profile
        </span>
    </a>
</li>
<li role="presentation" aria-hidden="true" data-view-component="true" class="ActionList-sectionDivider"></li>
<li data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
</li>
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.prettify())