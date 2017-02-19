from django import template


register = template.Library()

@register.inclusion_tag('blogs/pager.html')
def pager(page, page_view=2):
    page_num = page.number
    paginator = page.paginator

    pages_list = [x for x in range(page_num - page_view, page_num + page_view + 1) if x >= 1 and x <= paginator.num_pages]
    if pages_list[0] != 1:
        pages_list.insert(0, 1)

    if pages_list[-1] != paginator.num_pages:
        pages_list.append(paginator.num_pages)

    if len(pages_list) >= 2:
        if pages_list[1] >= 3:
            pages_list.insert(1, '...')

        if pages_list[-2] < paginator.num_pages - 1:
            pages_list.insert(-1, '...')

    return {
        'page_current': page,
        'pages_list': pages_list,
    }