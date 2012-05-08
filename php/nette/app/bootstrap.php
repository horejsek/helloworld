<?php

use Nette\Application\Routers\Route,
	Nette\Application\Routers\SimpleRouter;


// Load Nette Framework
require __DIR__ . '/../lib/nette.min.php';


// Configure application
$configurator = new Nette\Config\Configurator;

// Enable Nette Debugger for error visualisation & logging
$configurator->enableDebugger(__DIR__ . '/../log');

// Enable RobotLoader - this will load all classes automatically
$configurator->setTempDirectory(__DIR__ . '/../temp');
$configurator->createRobotLoader()
	->addDirectory(__DIR__)
	->register();

// Create Dependency Injection container from config.neon file
$configurator->addConfig(__DIR__ . '/config.neon');
$container = $configurator->createContainer();

// Setup router
$container->router = new SimpleRouter('Articles:default');

// Run the application!
$container->application->run();
