<?php //netteCache[01]000400a:2:{s:4:"time";s:21:"0.96113500 1336497599";s:9:"callbacks";a:2:{i:0;a:3:{i:0;a:2:{i:0;s:19:"Nette\Caching\Cache";i:1;s:9:"checkFile";}i:1;s:78:"/home/michal/Desktop/helloWorld/php/nette/app/templates/Articles/default.latte";i:2;i:1336496993;}i:1;a:3:{i:0;a:2:{i:0;s:19:"Nette\Caching\Cache";i:1;s:10:"checkConst";}i:1;s:25:"Nette\Framework::REVISION";i:2;s:30:"eb558ae released on 2012-04-04";}}}?><?php

// source file: /home/michal/Desktop/helloWorld/php/nette/app/templates/Articles/default.latte

?><?php
// prolog Nette\Latte\Macros\CoreMacros
list($_l, $_g) = Nette\Latte\Macros\CoreMacros::initRuntime($template, 'wxiail4wmd')
;
// prolog Nette\Latte\Macros\UIMacros
//
// block content
//
if (!function_exists($_l->blocks['content'][] = '_lbfb6a621c84_content')) { function _lbfb6a621c84_content($_l, $_args) { extract($_args)
?><h1>Articles</h1>

<ul>
<?php $iterations = 0; foreach ($articles as $article): ?>
	<li><a href="<?php echo htmlSpecialChars($_control->link("article", array($article->id))) ?>
"><?php echo Nette\Templating\Helpers::escapeHtml($article->title, ENT_NOQUOTES) ?></a></li>
<?php $iterations++; endforeach ?>
</ul>
<?php
}}

//
// end of blocks
//

// template extending and snippets support

$_l->extends = empty($template->_extended) && isset($_control) && $_control instanceof Nette\Application\UI\Presenter ? $_control->findLayoutTemplateFile() : NULL; $template->_extended = $_extended = TRUE;


if ($_l->extends) {
	ob_start();

} elseif (!empty($_control->snippetMode)) {
	return Nette\Latte\Macros\UIMacros::renderSnippets($_control, $_l, get_defined_vars());
}

//
// main template
//
?>

<?php if ($_l->extends) { ob_end_clean(); return Nette\Latte\Macros\CoreMacros::includeTemplate($_l->extends, get_defined_vars(), $template)->render(); }
call_user_func(reset($_l->blocks['content']), $_l, get_defined_vars()) ; 